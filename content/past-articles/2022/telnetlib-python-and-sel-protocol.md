Title: Telnetlib, Python, and SEL Protocol
Date: 2022-01-26 16:32
Modified: 2022-01-26 16:32
Tags: Python, SEL, Communications, Telnet, Libraries, Monkey-Patch
Category: Python
Slug: telnetlib-python-and-sel-protocol
Authors: Joe Stanley
Summary: Python's telnetlib library doesn't like null-characters, SEL protocol does, that makes for some interesting challenges.


### Zeros don't matter, right?

Well, that depends on who, (*or what*) you're talking to. If it happens to be an SEL relay, those zeros are pretty important.

How important? Well, every byte tells a story... so that means that every zero is important.

### Where did this start?

We can take a few steps back. Go take a look at [my article introducing SELProtoPy](/reading-data-with-selprotopy.html) to see
what the buzz is all about. In short, I want to write a full protocol client in Python for SEL Fast-Meter, and potentially branch
out from there. We'll see how far I can take it.

This is definitely an article that I've been wanting to write for some time, because it's very fascinating. Last year, I started
working on the project and began writing the protocol parser from specifications provided by an
[SEL application guide](https://selinc.com/api/download/5026/) which describes the intricacies of the binary SEL Fast-Meter
protocol.

Before I describe the challenges in too much detail, however, perhaps I should summarize SEL protocol...

----

> When we talk about SEL protocol, we're really discussing a *suite* of protocols which includes:
>
> * Fast Meter
> * Fast Message
> * Fast Operate
>
> Those "protocols" are all very closely linked, and are all intended to be "described" protocols. In other words, SEL protocol is
> self-describing. It essentially defines one "main" command/response sequence which then provides the definition for each of the
> various sub-protocols. SEL protocol commands all start with the hexadecimal-encoded byte `A5`. Each command is two bytes in length,
> and the "device definition" command will return a definition of all the other available commands. That is, a device wishing to
> query an SEL protocol enabled device would issue the hexadecimal string: `A5 C0` and interpret the response to determine what other
> commands are available for the device. The response from the device definition command not only provides a listing of what commands
> are supported, but what hexadecimal string is required to query for those commands.

----

So with the basics recounted, where this gets interesting comes into play when we account for the fact that SEL protocol was originally
a serial-based protocol, and made extensive use of null-padding, which is the practice of using zeros to separate content to account
for reasonable byte-alignment. That means that in almost every command response, there's a significant number of null characters (zeros)
in not only the definitions, but the data regions provided.

The application-guide I mentioned earlier has become something of the "de facto standard" for the protocol suite, and it defines how
SEL protocol provides the numerical quantities used to describe the power system. In many cases, it's possible for those quantities
to be zero for analog measurements. Whats more, SEL protocol provides an extensive set of word-bits (boolean points) in a bit-packed
format (8 word-bits packed into a single byte).

Let's pause and think about that for a moment.

Eight boolean statuses packed into a byte; many dozens, if not hundreds, of bits packed into bytes for a single response. At least a
50/50 chance that each bit will be a 0 (false/deasserted). This all means that it's highly likely that one or more of the bytes will
be all 0's... a null-character.

When I was working on this project, pretty early on, I found something interesting; when I would issue commands to request fast-meter
data, I'd see that the total data length was significantly shorter than what the response message indicated it should be. After
digging in, and looking at a little Wireshark, I found that my usage of Python's `telnetlib` was effectively cutting the null
characters out.

A little googling, and it was further confirmed from an [answer on StackOverflow](https://stackoverflow.com/a/32616342/10406011)

#### *"*

> I stumbled in this same problem when trying to get data from an RS232-TCP/IP Converter using telnet - the telnetlib would suppress every 0x00 from the message. As Fredrik Johansson well answered, it is the way telnetlib was implemented.

<div style="text-align: right">
<h4><i>"</i></h4>
</div>

Luckily enough, there's a fantastic way to resolve this problem, you can actually play a few games with `telnetlib` to monkey-patch
functionality to retain null characters. Just check out this code snippet from that StackOverflow answer:

```python
import telnetlib
from telnetlib import IAC, DO, DONT, WILL, WONT, SE, NOOPT

def _process_rawq(self):
    """Alteração da implementação desta função necessária pois telnetlib suprime 0x00 e \021 dos dados lidos
    """
    buf = ['', '']
    try:
        while self.rawq:
            c = self.rawq_getchar()
            if not self.iacseq:
#                if c == theNULL:
#                    continue
#                if c == "\021":
#                    continue
                if c != IAC:
                    buf[self.sb] = buf[self.sb] + c
                    continue
                else:
                    self.iacseq += c
            elif len(self.iacseq) == 1:
                # 'IAC: IAC CMD [OPTION only for WILL/WONT/DO/DONT]'
                if c in (DO, DONT, WILL, WONT):
                    self.iacseq += c
                    continue

                self.iacseq = ''
                if c == IAC:
                    buf[self.sb] = buf[self.sb] + c
                else:
                    if c == SB: # SB ... SE start.
                        self.sb = 1
                        self.sbdataq = ''
                    elif c == SE:
                        self.sb = 0
                        self.sbdataq = self.sbdataq + buf[1]
                        buf[1] = ''
                    if self.option_callback:
                        # Callback is supposed to look into
                        # the sbdataq
                        self.option_callback(self.sock, c, NOOPT)
                    else:
                        # We can't offer automatic processing of
                        # suboptions. Alas, we should not get any
                        # unless we did a WILL/DO before.
                        self.msg('IAC %d not recognized' % ord(c))
            elif len(self.iacseq) == 2:
                cmd = self.iacseq[1]
                self.iacseq = ''
                opt = c
                if cmd in (DO, DONT):
                    self.msg('IAC %s %d',
                        cmd == DO and 'DO' or 'DONT', ord(opt))
                    if self.option_callback:
                        self.option_callback(self.sock, cmd, opt)
                    else:
                        self.sock.sendall(IAC + WONT + opt)
                elif cmd in (WILL, WONT):
                    self.msg('IAC %s %d',
                        cmd == WILL and 'WILL' or 'WONT', ord(opt))
                    if self.option_callback:
                        self.option_callback(self.sock, cmd, opt)
                    else:
                        self.sock.sendall(IAC + DONT + opt)
    except EOFError: # raised by self.rawq_getchar()
        self.iacseq = '' # Reset on EOF
        self.sb = 0
        pass
    self.cookedq = self.cookedq + buf[0]
    self.sbdataq = self.sbdataq + buf[1]
telnetlib.Telnet.process_rawq = _process_rawq
```

*Very interesting........*


### Parting Thoughts

This is one problem solved, but I've come across an interesting issue where sending the commands over Telnet is not
working, but sending the same commands over a plain TCP socket works without failure. Hmm... Weird. That one's
going to take some more research. I'll be sure to post what I find, when I find it!

If you have questions, thoughts, or just want to say "hi", feel free to drop me a note in my new comments system
below!

Title: Using Pipewire Link to Bridge the Gaps
Date: 2023-01-09 09:00
Modified: 2023-01-09 09:00
Tags: linux, audio, networking, pipewire, alsa, sound, terminal, command-line
Category: Audio
Slug: using-pipewire-link-to-bridge-the-gaps
Authors: Joe Stanley
Summary: I'm ready to manage my audio "wiring" a bit more virtually, these days, and I'm ready to do that with some of the cool new tools available in Linux. Luckily for me, Pipewire has some command-line applications that make doing that an absolute cinch! And what's better, I can do it from Python, and make it a little more automagic. Now THAT's what I'm talking about!

Are you a nerd like me?

Do you want to connect audio devices in a Linux system easily, programmatically, and with a little help from Python?

Ok, so you're probably not *quite* a nerd like me, but if you'd probably still find some value from hearing about this
cool sub-system in the Pipewire ecosystem.

-----

Pipewire composes ports on devices to provide a mechanism to make connections between outputs (sources) and inputs
(sinks). This makes it possible to connect applications and interfaces into any arbitrary connection set. There are even
great tools like [`qpwgraph`](https://gitlab.freedesktop.org/rncbc/qpwgraph) which make it possible to connect these
interface graphically, and make it all smooth and beautiful.

<img src="{attach}/images/pipewire-link/no-connections.png" width="100%" alt="qpwgraph on my system">

That graphical application is beautiful, but what if you want to make those connections a little more manually, or
(if you're like *me*), programmatically. Well, good news! Pipewire offers a whole system to make those connections from
the command-line.

### Enter `pw-link`

```bash
$> pw-link --help
pw-link : PipeWire port and link manager.
Generic: pw-link [options]
  -h, --help                            Show this help
      --version                         Show version
  -r, --remote=NAME                     Remote daemon name
List: pw-link [options] [out-pattern] [in-pattern]
  -o, --output                          List output ports
  -i, --input                           List input ports
  -l, --links                           List links
  -m, --monitor                         Monitor links and ports
  -I, --id                              List IDs
  -v, --verbose                         Verbose port properties
Connect: pw-link [options] output input
  -L, --linger                          Linger (default, unless -m is used)
  -P, --passive                         Passive link
  -p, --props=PROPS                     Properties as JSON object
Disconnect: pw-link -d [options] output input
            pw-link -d [options] link-id
  -d, --disconnect                      Disconnect ports
```

That's what the interface of the PW-Link command-line tool looks like. Simple, powerful, and *GREAT*.

Want to list the sources (outputs)?

```bash
$> pw-link --output --id
  36 Midi-Bridge:Midi Through:(capture_0) Midi Through Port-0
  43 v4l2_input.pci-0000_03_00.4-usb-0_4_1.0:out_0
  47 alsa_output.pci-0000_03_00.6.analog-stereo:monitor_FL
  49 alsa_output.pci-0000_03_00.6.analog-stereo:monitor_FR
  50 alsa_input.pci-0000_03_00.6.analog-stereo:capture_FL
  51 alsa_input.pci-0000_03_00.6.analog-stereo:capture_FR
```

Or... how about the sinks (inputs)?

```bash
$> pw-link --input --id
  35 Midi-Bridge:Midi Through:(playback_0) Midi Through Port-0
  46 alsa_output.pci-0000_03_00.6.analog-stereo:playback_FL
  48 alsa_output.pci-0000_03_00.6.analog-stereo:playback_FR
```

> Marvelous, isn't it?

But how about getting those links created? How's it done? Can it be done programmatically? *With **Python**?*

Heh.

Well, now it can!

### Enter `pipewire_python`

[`pipewire_python`](https://github.com/pablodz/pipewire_python) is the core grounds of a Python Pipewire wrapper. It was
created by [Pablo Diaz](https://github.com/pablodz) and offers some great functionality with Pipewire wrapped up in
Python. Unfortunately, it didn't yet have `pw-link` functionality to list, create, and modify links in Pipewire. That
said, I've been able to add some of the functionality. It's in-progress in a
[pull-request](https://github.com/pablodz/pipewire_python/pull/15).

The PR is only a draft at the time of this writing, however, I'm hopeful it will be something that I can open officially
within a few days, and will be able to merge before the end of the week. When it *does* merge, `pipewire_python` will
have functional support to list inputs, outputs, and links, and it will be able to create links as mono (single
channel) or automatic-stereo (automated Left/Right channel pairing) connections. It'll be simple!

```python
from pipewire_python import link
inputs = link.list_inputs()
outputs = link.list_outputs()


# Connect the last output to the last input -- during testing it was found that
# Midi channel is normally listed first, so this avoids that.
source = outputs[-1]
sink = inputs[-1]
source.connect(sink)


# Fun Fact! You can connect/disconnect in either order!
sink.disconnect(source) # Tada!


# Default Input/Output links will be made with left-left and right-right
# connections; in other words, a straight stereo connection.
# It's possible to manually cross the lines, however!
source.right.connect(sink.left)
source.left.connect(sink.right)
```

> Won't that be slick?

Needless to say, I'm very excited. I'm going to use this for an automated system designed to support a VBAN streaming
network built fully on Linux. It'll be a robust, low-latency audio streaming system for my home, and I won't have to use
the *"dreaded Microsoft Windows"*. Won't that be neat?

Stay tuned... I'll be sharing more on this project soon!
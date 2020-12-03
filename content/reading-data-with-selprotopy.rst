Reading Data with `selprotopy`
##############################

:date: 2020-11-22 19:02
:modified: 2020-11-22 19:02
:tags: Protocols, SEL, Python, Communications, Metering
:category: Python
:slug: reading-data-with-selprotopy
:authors: Joe Stanley
:summary: Finally reading some data from SEL relays using Python! Now to get the controls working...


Still deep in the process of getting a fully functional SEL protocol binding suite in Python, but,
hey! At least I can write a little update on what's been going on!

(if you haven't read my article on what `selprotopy` is, take a look `here`_)

.. _here: https://blog.stanleysolutionsnw.com/sel-protocol-coming-to-python.html

In the past month of so, I've been able to really "whack out" some reasonable functionality. In
fact, I've been able to poll an SEL-351 for both digital and analog data. For those of you who
are a little familiar with SEL protocol, that means that I've been able to create a parser for
the relay definition block, and the various fast-meter blocks in addition to the DNA definition.
To boot, I've even tested (albeit breifly) on an SEL-751 and saw pretty promissing results.

That's all pretty good, but the eventual goal (well, *my* eventual goal) is to be able to poll
regularly and send commands/controls as needed. I'd also like to be able to read CEV reports
(more on that in the future) and perhaps the relay's SER (Sequential Event Recorder). So, is any
of the control functionality working yet? Not really...

I've gotten to the point where the commands *should* be configured and sent correctly to the
relay, but no dice.

Somewhere along the lines, I've clearly "bugged" something up. So now, it's really just a matter
of doing some additional debugging. Hmm... will need to get started on that. Trouble is, I've got
lots of other fun projects to work on too!!!

C'mon, Joe; wrap this thing up...
---------------------------------

Okay, so I'm rambling; at this point, I'm pretty excited to say that I've got some polling working
with `selprotopy`, but there's clearly some more to work on. I'm hoping that I can get commands
working here pretty soon, and then I've got a handful of options as the next step.

I could:
========

- create a system to read the SER
- get the CEV reading figured out
- start testing on a variety of SEL relays (but this would require testing a FOSS project at SEL,
  so I'm still not sure about this one)
- get an automated test suite built on my local GitLab instance

Clearly some more work coming, so stay tuned!
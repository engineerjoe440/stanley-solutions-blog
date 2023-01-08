Title: I'm Giving Up on Low-Level Audio in Linux
Date: 2023-01-08 10:00
Modified: 2023-01-08 10:00
Tags: linux, audio, networking, pipewire, alsa, sound
Category: Audio
Slug: giving-up-on-low-level-linux-audio
Authors: Joe Stanley
Summary: I'm so fed up with low-level audio in Linux. It's a constant struggle, and I'm throwing in the towel. I'm done.

**I *want* to love low-level audio in Linux.**

*I really do.*

But wow. It's atrocious! I'm so tired of fighting with `aplay` and `arecord` trying to figure out what the heck is
actually being presented to me. It's not intuitive, it's not robust, and for pity sake, I don't think it actually works.

So I'm giving up on *low-level* audio in Linux.

> Catch the drift?

That's right, I'm not done with *audio* in Linux. I'm done with ALSA.

<img src="https://i.imgur.com/ruxU5.png" width="100%" alt="seems about right...">

I'm sick of trying to figure out which device I should use, and how to plumb it through the rest of my system. It's a
constant uphill battle with ALSA. I'm calling it quits.

Luckily for me, there's Pipewire. *Beautiful, perfect, glorious, Pipewire.*

Pipewire bridges a gap that seems so perfect. It takes all of the lessons the Linux community has learned from ALSA,
PulseAudio, and JACK and introduces something new. I know what you might be thinking: "something else, *new*? Great..."
But it's not just new *to be new*. It's new to fix all of the mistakes from those older systems. PulseAudio is great,
but it's often too simple. JACK is great for audio pros, but often is too much to just *dabble* in. And ALSA?

> Let's not talk about ALSA anymore, shall we?

Ok... so it's true that ALSA is still being used underneath Pipewire, but *we* don't have to deal with that nonsense.
The Pipewire system takes care of all that garbage for us.

I'm going to have a whole slew of articles to follow this one, introducing lots of neat things with Pipewire, but for
now, let me introduce you to a few cool things.

### Pipewire "Guide"

I can't say whether this is the *definitive* guide to all things Pipewire, but it's a great resource, and it covers most
of the great tools I like to utilize: https://github.com/mikeroyal/PipeWire-Guide

### Pipewire Graph

Ok, one thing I picked up from JACK was its super-neat graph utility. It's something I really enjoy to visualize the
connections. I must be a bit old-school, huh? Well, there's something just as slick for Pipewire, actually, there's a
few resources, but my preferred choice is [QPWGraph](https://gitlab.freedesktop.org/rncbc/qpwgraph). It's just stinkin'
awesome, if you ask me.

Check out how it looks on my system! Granted, nothing's happening here, but it's still a good reference to see the
default view!

<img src="{attach}/images/pipewire-link/no-connections.png" width="100%" alt="qpwgraph on my system">
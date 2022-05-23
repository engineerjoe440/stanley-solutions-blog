Title: Home Automation... Condensed!
Date: 2022-05-23 15:23
Modified: 2022-05-23 15:23
Tags: linux, python, self-hosting, home-automation, iot, esp8266
Category: Home-Improvement
Slug: home-automation-condensed
Authors: Joe Stanley
Summary: Seems that, these days, there's an endless number of things that need to be automated for an "all-out" home-automation system. But how should we bring all of that stuff together? Well, I think I've got an idea...


As you may already know, I've been doing lots to automate my home. It's come to the point that my mother and other family members complain that they
can't do anything in my house without me. Well, that's left me with a bit of a conundrum. How can I make it so that people can use the home-automation
things, but not need any of the nuianced nonsense?

## All of the Audio

I've been working to make the audio "network" in my home quite extensive. Between use of [VBAN](https://vb-audio.com/Voicemeeter/vban.htm) for digital
audio streaming between my study and living room ([read more here](/networked-audio-using-vban-and-rpi)), and analog connections from my study to
kitchen, lab, and (yes) even bathroom. Now, the challenge with all that is that it's still highly reliant on my desktop or cell phone as the main source
of audio. Additionally, whenever I have virtual meetings in my study, I need to shut everything down around the house. Not very much fun.

I decided that I need a central control to allow easy Pianobar playback control, in addition to a "master mute" button that'll disable all audio streaming
around the house. Now... I'm still working on the actual "control box" which will have all of the buttons, but the operational pannel is already set up.

<img src="{attach}/images/home-automation-center/ima_3d778f5.jpeg" style="width: 100%" alt="Audio Output Blocks">

Since my analog stream is in stereo, I - of course - need to have four sets of terminals to make wiring easy. That's what's shown in the above picture;
there's one for +R, -R, +L, and -L. Everything we need! They all connect to an input block by way of an ESP-8266 relay-breakout-board (shown in the upper-right
of the image below).

<img src="{attach}/images/home-automation-center/ima_eec766f.jpeg" style="width: 100%" alt="Audio Connector Control">

When I get this set up (completely) the little ESP board will listen for [MQTT](https://mqtt.org/) commands from my home-automation server that will tell it
to open the normally-closed relay contacts and effectively shut down the whole analog audio network by disconnecting my study mixer from the rest of the
house.

## Detecting Doorbell Use

In my house, the doorbell is a bit difficult to hear from anywhere other than the livingroom. I mean, it's possible to hear it from around the house, but not
always. When I'm in the kitchen, if I'm cooking (which is often what I'm doing when I'm waiting for the doorbell), I can't often hear the bell over my skillet!
So, I want to integrate the doorbell detection into some more intelligent operations and be able to send push notifications or even play audio chimes through
the centralized audio system. Shouldn't be difficult, but I need to interface with one of my little [Technologic TS7500](https://www.embeddedts.com/products/TS-7500)
computers. Now... this computer has a 5VDC input. Not exactly ideal when the doorbell is running at about 16VAC.

<img src="{attach}/images/home-automation-center/ima_c71dcbc.jpeg" style="width: 100%" alt="Doorbell Conditioning Circuit">

Thus, another part of my home-automation center was built up. I needed to consume the AC input, run it through a bridge rectifier (the grey square on the right),
apply a little filtering and smoothing with a "reasonably big" capacitor, and then shove that into a 12VDC relay.

> and why, Joe, didn't you just use an AC relay?

Erm... I don't really have a good answer for that other than the fact that I had all of these components on-hand, and it seemed like fun.


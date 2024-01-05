Title: Python, Pianobar, and MQTT?
Date: 2023-01-15 13:52
Modified: 2023-01-15 13:52
Tags: Python, Pianobar, MQTT, HTTP, Configuration, Pandora, Music, Streaming, Audio, Home-Automation, Home Networking
Category: Python
Slug: python-pianobar-and-mqtt
Authors: Joe Stanley
Summary: We know that I'm something of an audio buff. I love having music around me all the time. But isn't that becoming more of a staple in the American home, anyway? I certainly think so. There's lots of folks who are also listening to music all the time. I have my own personal preferences, though. (Shocker, I know.) The thing is, I want my audio system to tie nicely into my home. I want play/pause buttons scattered around, and well... I've got more demands.

> Joe? Have Demands?

Psh! I know... Right? It's surprising... ***NOT***

Anyway... I want to have music streaming in my home, but I want it to meet some requirements:

* I want to play Pandora using [Pianobar](https://github.com/PromyLOPh/pianobar) -- The wonderful Linux-terminal, Pandora internet radio client.
* I want to control the application over MQTT
* I want to control the application over HTTP
* I want the application to be resilient and restart itself if things go... awry
* I want the application to give me information about what's playing
* I want the application to be built with a modern Python framework

> So... What exists, already?

Well, there's actually some pretty neat tools already out there:

* [Pithos](https://pithos.github.io/)
* [Pianod](http://deviousfish.com/pianod/)
* [Standalone Pandora Player](https://hackaday.com/2012/09/20/how-to-build-your-own-dedicated-pandora-radio/)
* [Pandora's Box](https://www.instructables.com/Pandoras-Box-An-Internet-Radio-player-made-with/)
* [Volumio](https://volumio.com/en/)

Unfortunately, for one reason or another, none of these really meet my objectives. In fact, I want to go on a rant some other time about why *Volumio* doesn't
really meet my needs as a tinkerer/hacker/general-nerd-extraordinaire.

## My Solution?

So glad you asked...

I decided to write my own tool. Because that's *just what I need*. Another project in my life. You know... because of all this free-time I have.

So, this project of mine will leverage the fantastic ecosystem for Pianobar, allowing me to interact with their phenomenal system of control and monitoring,
and I'll add to that an MQTT and HTTP interface. Both the MQTT and HTTP interfaces will allow simple control, real-time information, and more!

I started this project back on December 26th, and I'm actually quite proud of how far it's come! I really am tailoring this just for me, but at the same
time, I'd like for this to be something that others could pick up and play with, so most of the configuration is customizable. Things like what the MQTT
topics are, what the MQTT broker uses for an IP address, etc. Those are all things that somebody could pick up and swap out in their own system.

I haven't fully deployed this, quite yet, but that's because I'm still working on getting some of the other Pipewire plumbing in place so that I can
deploy it on my home audio server. We'll get there, soon! I'm excited about that!

## Where is this thing stored?

Well, right now, I've put it all on my GitLab. I'm considering setting it up to push to GitHub automatically, that way I've got some move visible presence
for the project as a whole, but you can go visit it here:

> [https://gitlab.stanleysolutionsnw.com/engineerjoe440/pianobarplayer](https://gitlab.stanleysolutionsnw.com/engineerjoe440/pianobarplayer)

I've picked up some interesting learnings from the project as a whole, but since I've been doing a lot with those same learnings elsewhere, I'll be
writing some of my thoughts on configuration with TOML in Python soon!

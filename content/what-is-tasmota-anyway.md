Title: What is Tasmota, Anyway?
Date: 2022-03-23 22:34
Modified: 2022-03-23 22:34
Tags: Tasmota, IOT, Smart-Home, Open-Source, ESP8266, ESP32, Home-Automation, Wifi
Category: IoT
Slug: what-is-tasmota-anyway
Authors: Joe Stanley
Summary: I've had a handfull of friends and colleagues ask about Tasmota; what it is, what it does, how to use it, etc. So I thought I'd put together a little article to tell you about this AWESOME open-source IoT firmware, why I use it, and how you can get started with it too!


If I've talked to you at all in the past year or so, you probably already know that I've gone a little wild with the home automation thing. I've got
all sorts of "smart stuff" scattered around the house. Mostly to turn lights on or off, but I do have some more intelligent things too. But, I'm a bit of
a tin-foil-hat-wearer, I guess you could say. After all, I run my own local Home Assistant, and to tie in nicely, I also use a free-and-open-source
firmware for most of my IoT devices, a little, something called *Tasmota*.

## What is Tasmota?
[Tasmota](https://tasmota.github.io/docs/Getting-Started/) is an open-source firmware, developed for the ESP8266 and ESP32 microcontrollers manufactured by Espressif. It's a lightweight, multifunctional, and
fully featured smart-home software for nearly every IoT device you can think of. It supports both MQTT and RESTful API communications, meaning that it can tie into nearly every home automation system available today.

In particular, there's a few things that I really like about the project.

#### 1) Its Openness

It's absolutely fantastic to have such a wonderful, well developed project all floating out in the open. Tasmota started as a simple project built for
ESP8266 devices, but quickly expanded to work for just about any IoT devices that run on the Espressif chipset. All sorts of common, economical brands of
smart plugs, smart bulbs, and more are supported by Tasmota, all because they're built on the Espressif chip, and the Tasmota firmware core is open,
allowing for continued expanse and improvement.

Tasmota is all available on GitHub, stored in the open, improved by the many. Plenty of wonderful developers who are all working on the project, but
clearly, I'm caught up on the great utopian parts of it all, and overlooking the downsides and drawbacks of open source. But perhaps that's ok. Maybe
that's just what I need to keep the spirit, and maybe that's good for us all. I guess I'm digressing, aren't I?

#### 2) Its Feature Set

Tasmota's got some awesome features, too! From it's simple, easy-to-get-started-with web interface and configuration to its integration with MQTT, and
simple HTTP REST interfaces. Even it's fully baked-in console for configuration. Tasmota has all the features that the other modern IoT devices have,
and all in one place.

#### 3) Its Lack of Cloud Dependence

Did I mention that I've got a case of "tin-foil-hat-itis"? Well, it's a problem. Perhaps not such a "problem" but it does mean that most of my smart
things don't talk to the rest of the world. That does mean that I can't exactly take direct control of all of my home automation when I'm not at home,
but I think I like it that way. A little security, of sorts...

Having no reliance on the wild inter-webs, it means that when things go down (like my connection to the internet), I still have control of all my things.
Well, until I break things (as per the usual).

## Wrapping Up

I'm a big fan of open source (clearly) and if you're ever looking to make your home a little smarter, let me recommend you take a look at Tasmota!

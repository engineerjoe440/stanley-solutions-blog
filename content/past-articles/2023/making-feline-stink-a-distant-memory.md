Title: Making Feline Stink a Distant Memory
Date: 2022-08-04 15:52
Modified: 2022-08-04 15:52
Tags: arduino, electro-mechanical, smart-home, development, platformio, pets, exhaust
Category: Home-Improvement
Slug: making-feline-stink-a-distant-memory
Authors: Joe Stanley
Summary: We all love our pets, but nobody likes cleaning up after them when they "do their business," right? Well, I'm in that same boat. It's the reason I have a "Cat Closet," where my automatic litterbox is located. Trouble is, when he uses it, that thing gets to stinkin' - and pretty quick too! Thus, I've come to a resolution with a new home-automation system. I call it "ScentAssist." Let me explain...
Gallery: {photo}scentassist

<img src="https://raw.githubusercontent.com/engineerjoe440/ScentAssist/master/logo/ScentAssist.png" style="width: 40%; margin: 10px;" align="right" alt="ScentAssist">

Like I said, we all love our pets, but sometimes the "stink" can be overwhelming. *Especially with cats...*

My little "Cat Closet" helps to keep things somewhat isolated, but it produces a new challenge: all of that stink gets trapped ***indefinitely***. That's... well, less than
ideal in just about any situation. So I came up with a solution that I call [`ScentAssist`](https://github.com/engineerjoe440/ScentAssist). In a nutshell, it's an automatic
fan. Nothing crazy, but it's SUPER helpful, and pretty simple!

<img src="{attach}/images/scentassist/ima_1a16017.jpeg" style="width: 100%;" align="right" alt="ScentAssist">

So, with a system that's not really IoT, but is embedded, I wanted a very predictable routine configuration. I wanted the system to be predictable, and work without too much
fuss.

> *asside:* I'm still working on that last part, but I'll get to that later...

With this desire in mind, I opted to base my system around a relatively simple state-machine.

::uml:: format="svg" alt="ScentAssist State Machine" title="ScentAssist State Machine" width="100%"
    !theme crt-green
    hide empty description
    IDLE : Generic System State
    IDLE : (everything returns here)
    ACTIVATE: Turn on LED and relay
    ACTIVATE: to energize fan
    DETECTED: Condition turning on
    DETECTED: fan, or resetting
    DETECTED: delay timer
    RESET: Turn fan off, and
    RESET: restore default time
    RESET: counter values

    [*] --> IDLE : bootup
    IDLE --> ACTIVATE : User manually \nactivates fan
    IDLE -> DETECTED : Fully Qualified Motion \n Sensor Detection
    DETECTED --> ACTIVATE : Fan was already running, \n maximize running time
    DETECTED --> IDLE : Start countdown timer \n (delay after detecting a cat)
    IDLE --> RESET : Fan runtime elapses
    RESET --> IDLE
::end-uml::

So, that's all pretty simple, what *wasn't* simple (or should I say *isn't*, since I'm still working on it) was the motion-sensor qualification. I'm cheap, and a fan of
reusing old parts, so I pulled out an old 12VDC power supply from my "storage." It was originally from an RGB DJ light that I tore apart and hacked. Don't get me wrong,
the power supply is reasonable, enough, but it's not exactly... "clean." The output is a bit noisy. In fact, I've had trouble with these things before. I've used its
brethren before (that's right, I had like 8 of these things, at one point) and they *worked*, but gave me trouble. So with all that noise, the motion sensor drives some
funny behavior on its output.

I'm using little motion sensors like the one pictured below; they're simple enough, +/- voltage rails, and an output. The output provides a little less than a solid
digital signal, so I hooked it up to one of the analog inputs on the Arduino. No biggie. However, with all that noise from my friend the 12V supply, the output signal
becomes a bit...

messy.

[![motion sensor](https://m.media-amazon.com/images/I/41AkdTj2yML._AC_SL1001_.jpg)](https://www.amazon.com/gp/product/B096NZ4P3K/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)

Still, it's not unreadable. I can pretty easily detect the step-change when visually inspecting the waveform, or watching the analog readouts from the Arduino, itself. Just
need to filter out all that garbage. Sure! Analog filtering is pretty easy. Right?

**...**

> *Right...?*

It was easy when I was in college, and had just learned the stuff. But I haven't touched algorithms like IIR (Infinite Impulse Response) in about three years! So,
needless to say, I was a bit rusty. Still am... in fact. The filtering I built still isn't *quite* where I want it, but I'm close. Should just be a few more tweaks, and
then I'll be able to call this project complete!

When I do complete it, I'll be sure to bring some more thoughts to this article (below), but for now... enjoy the few project photos!

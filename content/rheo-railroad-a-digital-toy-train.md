Title: RheoRailroad - A Digital Toy Train Set
Date: 2022-08-23 17:00
Modified: 2022-08-23 17:00
Tags: Arduino, Electro-Mechanical, Smart-Home, Development, PlatformIO, Toy-Trains, Lionel, Model-Railroading, ESP8266
Category: Model-Railroading
Slug: rheo-railroad-a-digital-toy-train
Authors: Joe Stanley
Summary: Model railroading has always played close to new technology. I mean, after all Lionel used an electric motor back when they were still relatively new to make the first electric toy train. I'm continuing in that tradition, but doing it at my own speed, making an electric toy train speed-control that I can control from the palm of my hand. That's right, from my phone!
Gallery: {photo}rheo-railroad

Well, I'm fairly certain that I've discussed this before. But on the off chance I haven't. I like trains.

Yep, I'm one of those guys.

When I was little, I remember spending countless hours with Thomas the Tank Engine playing so many wild adventures. But I also remember playing as many,
if not more, countless hours with my Lionel Toy Trains. Those little electrical wonders. A teensy, tiny little motor, a handful of electric lights, and
a really slick looking little die-cast metal body, and those trains were basically real. it's sort of a Christmas tradition for lots of families to set up
a little Lionel layout around the Christmas tree. Now that I have my own house, it's no different for me! I've got my little loop of track, and my
great-uncle's postwar Lionel Berkshire, all steamed up and ready to entertain!

> Me. Entertain me. That's about it.

Anywho...

Those Lionel trains are pretty slick with their bells, and whistles, but I thought I'd try something different. There's these new-fangled things called
microcontrollers, and they work really well with this magic called WiFi. Have you heard of it? So I thought I'd give it a whack.

---

You probably already know that I'm an avid home-automation enthusiast. I host a bunch of my own web-services, and I have my Home Assistant running on an
ancient x86 PC (yeah, you can hear the spinning rust any time I ask it to do something). So I thought it would be neat to take it a step further, and
automate my little toy trains. Mind you, Lionel's already gotten this perfected. They have a *way-cool* system called TMCC with their "Legacy" remote.
They've even got bluetooth! Wild, huh? Well, that would all be well-and-good, except for the fact that I need to control OLD trains. Remember what I said
earlier?

> "My great-uncle's postwar Lionel berkshire"?

Yeah. That.

---

Well, that wasn't going to stop me. I thought I'd build my own control. I could get all slick-and-fancy and build some cool digitally-controlled, smart
power-supply; but where's the fun in that? Actually, I just didn't feel like doing the math, required... but maybe another time.

I decided to use one of Lionel's early control mechanisms, a manual rheostat! That's right, they made variable resistors to slow down, or speed up those
old trains. What's advantageous of that old system *for me*, however, is that it's a linear device. I mean, it moves in a straight line from one extreme,
to the other. That means that I could take it and add some jurry-rigged control systems. Namely, a piece of all-thread, and a stepper motor, controlled
by a driver board and an ESP8266.

<img src="{attach}/images/rheo-railroad/ima_d0da9c3.jpeg" alt="Rheo-Railroad Control">

### Neat, huh?

So that's one of the things I've been working on, as of late. Working on my own Lionel Toy Train control. I've still got plenty of work to do (isn't that
what I always say, anymore), but it's a start! Just need to do the programming, now, and I think I'll be able to nail that with PlatformIO and some
handy-dandy ESP8266 libraries. Gosh, I love libraries!

Let me know what you think in the comments, below! Use those comments! That computer in my basement isn't just sitting there for nothin'!


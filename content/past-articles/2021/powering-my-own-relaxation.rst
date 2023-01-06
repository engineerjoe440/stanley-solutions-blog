Powering My Own Relaxation
##########################

:date: 2021-06-19 11:40
:modified: 2021-06-19 11:40
:tags: Ammo-Can, Power-Supply, Arm-Chair, Linux, Charger
:category: Home-Projects
:slug: powering-my-own-relaxation
:authors: Joe Stanley
:summary: I spend enough time in my arm-chair with my laptop that I thought it about time to power all my digital toys in the same spot!


You know, I never thought I'd spend so much time in my arm-chair. But here we are.

It's become pretty comfortable, recently, with all the new audio networking I've been working on (namely my audio network using VBAN - you can read
more about that `here <https://blog.stanleysolutionsnw.com/spam-the-vban-for-non-stop-audio.html>`_). Still, I'm not about to just sit back and listen
without doing *something*. I mean, c'mon! I'm an insatiable tinkerer, after all. So, I spend a lot of time working away on my laptop (really starting
to love `KDE Plasma! <https://kde.org/plasma-desktop/>`_) and poking around at random bits and bytes.

So I need a charger, but I get bored dragging around that plain ole' wall-wart! So I thought I could do one better. I've seen plenty of those neat
looking amo-can stereos, online, but that's not quite my style. If you know me, you know I prefer cabinet stereos. No, instead I thought I could put
all of my power supply components in the can; and throw in a few of my own touches along the way. So, I decided I'd get to work.

A little too much drooling and visitation of our favorite, least-favorite A-to-Z online marketplace, I had an assortment of nerdy-looking switch
assemblies, voltage meters, and a beefy little multi-output DC power supply.

.. image:: {attach}/images/demo-boards-and-amo-power/203727287_161197975998707_4701277717982762523_n.jpg
   :alt: The Controls of my "Unique" Power Can
   :width: 600 px

Now with all these neat little switches, I've got to do ***something*** with them, right?

You bet!

How about adding a little Linux computer, to the mix? Sure! I gave yet another old machine new life by taking an old
`Technologic computer <https://www.embeddedarm.com/>`_ and lobbing it into the case; mounted with Ethernet, serial terminal, and dual USB ports exposed
for easy access. My own sort of computer tower, you might say.

.. image:: {attach}/images/demo-boards-and-amo-power/203630587_497812148003314_6021780960392169872_n.jpg
   :alt: Mounted a Linux computer in there too!
   :width: 600 px

But this thing's ultimately a power supply, right? So it's got to have *power*! And that, it does! Inside, I've mounted a little multi-output power supply
with 3 discrete taps; 24V, 12V, and 5V. I don't quite know what I'm going to do with 24V, yet, but the 5V and 12V are already serving my purposes to power
the little computer, a variety of lights, and perhaps a few more odds and ends as time progresses.

.. image:: {attach}/images/demo-boards-and-amo-power/203150896_2002088606597054_7741904286201403555_n.jpg
   :alt: The power!
   :width: 600 px

What's more, however, is that I've also inserted several USB power hubs, and mounted a computer charger inside the can so that I can power my laptop, too!
In fact, as I sit her writing, I'm using the power supply right now!

Now, I'll grant that like so many of my little tinkering projects, this one is nowhere near being complete, but I will say that *one* of the switches
does function to control the two voltage meters mounted inside (one analog, the other digital).

.. image:: {attach}/images/demo-boards-and-amo-power/202866327_175178427900304_1831963921642931273_n.jpg
   :alt: The final (but not finished) product!
   :width: 600 px

Specs:
------

So let's talk about what all's in this thing!

Power Supplies:
~~~~~~~~~~~~~~~
* 2x 5V, 2.1A USB Chargers
* 2x 5V, 2.4A USB Fast Chargers
* 1x 19V, ~2A Computer Charger
* 2x 120VAC Outlets (one internal, the other external)
* 1x 24V DC Rail
* 1x 12V DC Rail (powers the USB chargers, and a few other bits-and-bobs)
* 1x 5V DC Rail (powers the Technologic Linux computer)

Switches:
~~~~~~~~~
* 3x Safety Toggle Switches
* 5x Illuminated Rocker Switches

Meters:
~~~~~~~
* 1x Backlit AC Panel Meter, 0-150VAC
* 1x Blue LED Digital Meter, 0-200VAC

Computing Specs:
~~~~~~~~~~~~~~~~
* 1x Technologic 7800 ARM Computer; Runs Pre-built Debian 5.0, "Lenny" (yeah, it's old, okay?!)

Final Thoughts
--------------

Another quick note about the project, I finally got to use my brand-new drill press for it! Woo-hoo!!! That was a lot of fun!

Hopefully, when I get the little computer tied into some more important things, I'll have more to say on the matter, but first, I've
got to get it booting Debian... Then see if I can possibly get it to run newer images... Like, I dunno, something *NEW*?!?!

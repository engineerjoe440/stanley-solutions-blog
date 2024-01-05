Title: Bringing Light to the... Living Room?
Date: 2022-02-27 09:52
Modified: 2022-02-27 09:52
Tags: esp8266, tasmota, smart-home, home-assistant, mqtt, iot, lighting, lights, development
Category: Home-Improvement
Slug: bringing-light-to-the-living-room
Authors: Joe Stanley
Summary: Shadow boxes deserve a shadow... right? Well, if there's a shadow, there has to be some light! That's what I've been working on; adding a little intelligent lighting to my shadow boxes! But, I've also been going crazy in the kitchen with some lights around the cabinets.
Gallery: {photo}shadow-box-lights

I've been working on adding all sorts of smart lights around my home since I bought it, and the progress doesn't slow down!
I've pretty much covered all of the things that can be automated with little smart plugs. Everything from my scentsy's to my lamps, but now,
I need to automate some of the more... challenging things.

I started a couple months ago with my coffee nook. I added a couple lights under the cabinet and hooked them up to a custom board, using an ESP-01S
to do my heavy lifting. I ran into a whole SLEW of issues with this. Drat! Everything from conflicting WiFi signals with my dual access points, to
blown out ESP modules, to faulty board designs. That's right, I incorrectly designed the board the first time around. *give me a dope-slap for that*

Turns out I'd left two pins on the ESP module floating (i.e., not connected to any power source or other electrical element), and they very much
needed to be connected to the Vcc node with a pull-up resistor. Should've looked more closely at those reference circuits the first time through.
Anyway, I've gotten that working now! Only took me two board-revs to get it done. Hah! We won't talk about the fact that the footprint of the board
as a whole isn't quite right... Another day...

I really do need to share my learning from that project, don't I?

#### I digress...

So, yesterday I finally wrapped up the project of adding smart control to some new lights for the shadow-boxes in my living room. I use some old
wooden crates for shadow boxes. They go very well with the rest of my "old stuff" around the house, and now they have even more character!

I picked up a set of [under cabinet LED lights](https://www.amazon.com/gp/product/B01LMSYUP4/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)
from Amazon, and some [12V DC supplies](https://www.amazon.com/gp/product/B00FEOB4EI/ref=ppx_yo_dt_b_asin_title_o04_s00?ie=UTF8&psc=1), combining
those with my little generic board, I was able to make some nice little controls.

<img src="{attach}/images/shadow-box-lights/ima_906029b.jpeg" style="width: 100%" alt="Imagination in a Box!">

I did struggle a bit with picking the right N-MOS transistor for controlling the LEDs. My go-to is a BUZ11A, which is normally good enough. It's
rugged, general-purpose, and packs a punch for current control ability. Trouble is, that with my boards, the voltages weren't quite right. I
discovered this late yesterday afternoon when powering up the little board and flipping the WiFi-enabled "on-switch", and the LEDs barely
illuminated enough to see a dim glow. Not ideal for a shadow box.

I scratched my head for a bit, and realized that the transistor's voltage thresholds weren't where I wanted them. Luckily enough, I had some options!
I dug around in my hoarder-size-stash of electronics and found a set of logic-level transistors which were better suited for the job. Still being
N-MOS, they were exactly what I needed. A bit of solder-wick later, I had my new transistors replaced, and my lights were working like a charm!

<img src="{attach}/images/shadow-box-lights/ima_5049e25.jpeg" style="width: 100%" alt="Illuminating my Imagination">

Now mind you, this isn't a story of all up-and-up success. This is the... third whack at the design. I started with some 4.5V supplies. Those were
ample for the control circuit, but not for the LEDs themselves (since they're rated for closer to 12V). I then thought I'd get clever and use a
boost converter to do my dirty work so I could leave the rest of the circuitry intact. Didn't I learn anywhere that it's tricky to use a boost
converter coming off a PWM-enabled circuit? Guess not.

Needless to say, both of those "adventures" were a bit less than ideal; but we got there! Third time's the charm!

#### Don't forget the kitchen!

Ok... Ok... I've also been working on illuminating the kitchen. I *seriously* need to sit down and tell you about what I've been doing with that
coffee nook light. Those are some "fun" stories.

Anyway, I had tried my hand at flashing Tasmota on some off-the-shelf WiFi-enabled smart LED controls. That failed pretty miserably. But those
controls were cheap, and I wasn't impressed anyway. I spent some serious time Googling around, and stumbled upon [ATHOM](https://www.athom.tech/)
which produces pre-flashed Tasmota/ESPHome/WLED-enabled boards in enclosures designed for makers and tinkerers like me! From browsing their
website, it's clear that English is not their first language, but I'm solidly impressed by their hardware. Simple, effective, and in clean packaging.
They worked great, right out of the box, and I didn't have to fight those dumb boards that don't already come with Tasmota flashed. MARVELOUS!

So... I went crazy with installing these things all over my kitchen for above and below each of the cabinets... Just take a look!

<img src="{attach}/images/shadow-box-lights/ima_4ee1367.jpeg" style="width: 100%" alt="Illuminating my Imagination">

That's basically the "orange" shade that Home-Assistant sets them with. But wow... when you come visit, remind me, and I'll show you the vibrance
of the blues, greens, and reds... it's stunning!


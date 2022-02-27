Smart Christmas Trains for a Smart Home?
########################################

:date: 2020-11-22 19:32
:modified: 2020-11-22 19:32
:tags: ESP32, IOT, Smart-Home, Automation, WIFI, Lionel, Vintage, Variac
:category: ESP32
:slug: esp32-controlling-lionel-trains
:authors: Joe Stanley
:summary: Finally, with my own home, I think I can return to my goal of having a Lionel train surround my Christmas tree, but perhaps I need to consider how I'm going to automate it...


For any railfans, a train surrounding a Christmas tree is something of a given. But I recently
came up with a conundrum...

See, my house is becoming more and more of a "smart home," and I'd like the Christmas holiday
to be much of the same. Now, that's pretty easy when it comes to the lights. Throw a smart-plug
running `Tasmota`_ firmware (a free and open source alternative to the proprietary solutions) at
those lights, and let the magic commence. But for toy trains around the tree? That's a bit of a
different story.

.. _Tasmota: https://tasmota.github.io/docs/

The problem:
------------

So, why couldn't I just throw another smart plug at my toy trains?

Well, I guess I *could*, but I don't really think that's the greatest idea. Reason being that
turning the trains on and off in a binary fashion (all or nothing) might not be great on them,
and wouldn't be the most pleasant sound either. I guess I could look at some of the solutions
that Lionel markets like their `Legacy`_ or TMCC options, but that would mean a lot of new 
purchases, research, and maybe some other annoyances that I'm just not too excited to deal with.
So, needless to say, that option's off the list too. Perhaps one of Lionel's new bluetooth
options? I guess, but that's kind of boring, don't you think? And to boot, if I were to follow
that route, I'd certainly need to buy a new locomotive, and I'd likely need to hack the remote.
Another option that I'm just not thrilled about.

.. _Legacy: http://www.lionel.com/brands/legacy/

Hmm... well, what's left? My pickyness hasn't left me with many options, but I think there's
still *got to be something*.


Think. Think. Think.
--------------------

I spent some time thinking about my alternatives today, and well, let me just walk you through
that.

I started out thinking about the toy train transformer itself. That's all it really is, a
transformer; well, *variac* specifically. A variac is just a variable transformer, essentially
a graphine brush that moves across the windings on the secondary side of a transformer. This
varying motion provides the variable "tap" on the transformer, and allows it to acheive a 
voltage that can be varied and controlled to change the speed of the connected trains.

It's pretty simple really, Lionel and others pioneered this practice for the model and toy scene
nearly a century ago. Trouble is, the transformers (in my case, a Lionel ZW transformer) aren't
exactly built for modification, and like I mentioned earlier, I don't exactly idolize the thought
of tearing apart my toy train controls just to make them "smarter."

.. image:: https://images-na.ssl-images-amazon.com/images/I/91SL6j6kkNL._AC_SX425_.jpg
   :alt: Here's what a variac looks like...
   :width: 350 px

I spent some time looking around for a cheap (I'd like to stay under $100 since I need to buy gifts,
too!) variac that is digitally controlled. No dice.

I guess I could buy a big variac and hook up a motor and...

No.

Not gonna fly.

Hmm... well, what else?

Another option is a rheostat. For those of us who either forgot or skipped electrical machines in
college; a rheostat is basically a variable resistor. Similar to a variac, rheostats are typically
made from some form of wound wire that has a varying resistance as the user employs a sweeper to
move from one end to the other. That's really the big difference, and the reason it's not just
called a variable resistor, or even a potentiometer. Rheostats are basically "variable resistors
on steroids," built for high-energy systems.

.. image:: https://cdn.images.fecom-media.com/A49116.jpg
   :alt: And this is a rheostat...
   :width: 350 px

So... yours truly started poking around online looking (once again) for a cheap electrical
device beefy enough to run toy trains, but not so big that it would break the bank. I bummed around
through Amazon with no luck, but after a quick search on eBay, I found something pretty enticing...

Guess which toy train company just happened to make rheostats way back in the day?

That's right! Lionel rheostats!

.. image:: https://image.invaluable.com/housePhotos/SeymourAuctions/95/563895/H4246-L72135272.jpg
   :alt: A Lionel rheostat!
   :width: 450 px

A solution?
-----------

So, is that it? Just like that? Problem solved?

Well, yes; but also, no.

Lionel rheostats seem to be running about $10 and about as much in shipping on eBay at the time of
writing, so that's really good news. Not to mention the fact that they were built *specifically
for toy trains* (score!).

But what about the fact that it's mechanical, not digital?

I knew you'd ask that...

Well, here, the big difference is the form factor. These rheostats are significantly easier to
interface with. Since they're linear, a single piece of all-thread-rod and a little stepper motor
could quite easily do just what I need. I could connect a little stepper motor to an ESP32/ESP8266
and hook that up to a Lionel rheostat via all-thread and a moving nut with a sweeper attached.

Easy-peasy! Well, sort-of.

What's next?
------------

Well, there's still quite a bit left on this one, and a good chance I won't actually do anything
about it this Christmas. Still, it's an exciting idea, and I'm definitely going to pursue it!

That's all for now, but stay tuned!

Who knows, maybe I'll even throw a whistle control on there!!!

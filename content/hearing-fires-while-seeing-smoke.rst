Hearing Fires While Seeing Smoke
################################

:date: 2021-07-12 20:18
:modified: 2021-07-12 20:54
:tags: Wildfire, IoT, MCU, Mesh, Radio, Smart-Sensor, Capstone, University
:category: Capstone
:slug: hearing-fires-while-seeing-smoke
:authors: Joe Stanley
:summary: While most of North Idaho is seeing (and smelling) plenty of smoke, I'm looking back over a successful Capstone project and more to come...


If you've talked to me at all in the past nine months or so, you probably already know that I had the great privilege of sponsoring an Engineering
Capstone project at the University of Idaho. Now, admittedly, it's something of a selfish endeavor as I have far too many "fun things" that I'd like
to explore, and not enough time or energy to do them all. Thankfully, some good faculty members are just as excited about some of these intriguing
projects as I am.

What's more, though, as I sit here in North Idaho, surrounded by worsening smoke from many terrible wildfires, I'm reflecting on the project I was
so lucky to sponsor, and how excited I am for its future, and what future students will bring to it.

The Project
-----------

So what was it? Well, the project in a nutshell was to lay the groundwork for a design of a device which will detect wildfire using infrasonic sound;
that's the sound that's lower than what we can hear - think that death rumble from that old beater car you drove in high-school. No? Just me? Oh...

The infrasonic sound would be detected by an ultra-economical (yeah, cheap) condenser microphone and amplified before being measured by a small
microcontroller responsible for wrapping that data up into a message sent over-the-air back to some central base. But what's to make it more interesting,
this wireless message is to be sent over a mesh network of these devices. Think hundreds... no, thousands of these little devices scattered around the
forest, all taking readings at specific intervals and relaying that information back to us so we can *hear* if there's a wildfire starting anywhere.

If this all sounds familiar, it's probably because I've already `told you all about it <./wildfire-prevention-with-sound>`_. This project is one that
was started a few years back at the `University of Idaho <https://uidaho.edu/>`_ and was discontinued due to a lack of funding and support. Luckily
the sponsoring professor was still just as interested as I was, so we were able to pick it back up and continue down the road to developing some really
neat tech.

This Year's Team
----------------

.. raw:: html

   <img src="{attach}/images/team-firewatch.jpg" width="400" alt="Meet Team Firewatch!" align="right">


So, this year, we had a team of some really outstanding students from a variety of backgrounds. Meridian, a mechanical engineer; Carlos, a computer
scientist; and two electrical engineers, Cory and Drew. We had the luxury of giving this fantastic team the flexibility of choosing their own path
in terms of the areas they were really interested in researching, which made for a lot of fun.

I was really impressed by these students and their willingness to work so hard on this project. They produced some really fantastic work, and I get
the pleasure of keeping it! At least... until next year, when we get some more students to work on it.

The Product
-----------

.. image:: http://images.shoutwiki.com/mindworks/thumb/5/5b/2021_infrasonic_wildfire_detector_finished_enclosure.png/800px-2021_infrasonic_wildfire_detector_finished_enclosure.png
   :alt: The sensor...
   :width: 600 px
   :align: left

The team was able to design a really wonderful and unique enclosure to encapsulate their microcontroller, sensor, antenna, and amplifier circuit. They
were also able to use some clear acrylic tubing to really show off how sharp this thing looks!

Now, I'm not going to go too-deep into the technical specs of this thing, partly because I don't want to type it all out, and partly because the team
has already done such a fantastic job documenting it both in their `Wiki page <http://mindworks.shoutwiki.com/wiki/Infrasonic_Wildfire_Detector>`_
and in their `GitLab repo <https://gitlab.stanleysolutionsnw.com/infrasound-detector/portfolio-2020-2021>`_ (which is one of the services I host!).

What's Next
-----------

The project is nowhere near complete (even as cool as that enclosure looks). So I'm already lined up to sponsor a continued Capstone program again this
year (so long as the University will let me!), and I'm very excited to do so. There's certainly a few key things that we still need to work out:

* Power - An obvious concern for any IoT device, and certainly one responsible for such a challenging environment.
* Sensor Validation - This years team did a great job bootstrapping their way up, but with luck, next year's team will be able to refine that work into
  something that can prove the validity of the sensor.
* Wireless Mesh Networking - This was something that was really exciting since this year's team was able to find an open-source library to help with
  this challenge, but there's more to be done; especially if the network is going to be anything larger than a few nodes.
* Enclosure Testing - Anything exposed to the elements needs to be hardened, and this enclosure still needs a little refinement there.


All that said, I'm really excited to see where this project continues to grow, and what this next year's group of students will be able to accomplish!

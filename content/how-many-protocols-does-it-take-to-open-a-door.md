Title: How Many Protocols Does it Take to Open a Door?
Date: 2023-12-25 14:45
Modified: 2023-12-25 14:45
Tags: Home-Automation, Home-Assistant, Mqtt, SEL, Sel-Protocol, Open-Source, Relay, Automation
Category: Home-Automation
Slug: how-many-protocols-does-it-take-to-open-a-door
Authors: Joe Stanley
Summary: It's just a garage door, right? It's just a switch, right? How hard can it be to automate it? In this article, I explore the connections between a number of projects which I've been working on for quite some time, now.


Holy smokes. Really? How many protocols *does* it take?

I'm about to find out.

---

A few years ago, I endeavored to start creating an SEL protocol parser in Python. Why? Well, because I want to use some second-hand protection relays for
a variety of my home-automation needs. They're ultra-robust, well-understood, and pretty much un-breakable. With all of that, they've got great (and simple)
input/output capabilities for both analog and digital needs. For me, that's excellent!

But why the protocol? Well, I've got to be able to talk to them, of course!

So way back in 2020 (yeah, Covid times) I started on [`selprotopy`](/sel-protocol-coming-to-python.html). It's a relatively simple system. At the time it
just used Telnet, and it was super rickety... I've recently updated the [documentation website](https://selprotopy.readthedocs.io/en/latest/) to use a
more modern theme, and to run on ReadTheDocs. But so far, I've only talked about one protocol. What others are there?

Well, a few years ago, I "hung" an older SEL-351S relay in my garage so that I could interface with the garage door openers. Realistically, it's only a
few hundred feet of cable (at most) from the relay's mounting point to the control-side in my house. Even with this short run, I decided that I'd prefer to
go with an RS-485 serial connection over the RS-232 form. After all, RS-485 can span much greater differences due to the nature of its differential signal.
This lead me down the rabbit hole of getting re-familiarized with RS-485. I've monkeyed with it, before, in a more professional setting, but only to test a
known-good system with a "questionable" one, so that was relatively straight-forward.

Here, at home, I wanted to interface my SEL-351S relay with a Raspberry Pi 4. To do this, I needed a 485 adapter. I started out with the
[Waveshare RS485 CAN HAT for Raspberry Pi](https://www.amazon.com/RS485-CAN-HAT-Long-Distance-Communication/dp/B07VMB1ZKH/), but as I came to learn, this
wasn't the best option for me, as it only supports a half-duplex connection (true RS-485). As I re-learned, the SEL relay that I'm interfacing with (as
all SEL relays) is a full-duplex device. That means that it can simultaneously receive and transmit data. That's part of what makes SEL protocol so neat.

So I sat with PuTTy and banged away, trying to get some form of communications, and only ever got gibberish.

> Not ideal.

I ended up picking up one of these [nifty little USB RS-485/RS-422 converters from Amazon](https://www.amazon.com/dp/B07B416CPK) to do a little more testing.
Sure enough, with a properly configured, full duplex system my relay became quite the chatty little box.

... or ... at least as chatty as an SEL relay can get. Which really isn't very chatty at all, actually.

So, after proving out my little theory. I decided that I should get something that would be a little easier to mount. That lead me to this *other* USB to
RS-485/RS-422 converter: [DSD TECH SH-U11F Isolated USB to RS485 RS422 Converter](https://www.amazon.com/dp/B083XSG1RG). That really did the trick, plus,
I could nicely mount it in my "lab control panel."

---

Wait a second. How many protocols are we up to?

Oh, right... only 2. (because I consider RS-485 its own protocol in this context)

That's not so bad, right? Well, I still haven't tied this system into the rest of my home automation!

---

To connect my system to the automation center of my home (my Home-Assistant instance), I'd like to use my trusty friend, MQTT!

So, I needed a little service to subscribe to the specific topics where my controls would be published. Not so bad. This little application would also need
to manage the SEL protocol control, and be easily modified (with a configuration file). So I pulled out my handy little Python cookbook and started one of my
famous "feverish coding sessions." That lead me to produce this little application:
[Lab-Automation](https://gitlab.stanleysolutionsnw.com/stanleysolutionsinfra/lab-automation/-/tree/master) Go have a look for yourself!

With this application, I'm able to read from a configuration file just exactly what topics I should be using, and how to interface them to the operations with the
relay. Really, it's a pretty simple pattern that I've used in a few places around the house, now. That's been very nice to re-use the pattern.

Now, to teach Home-Assistant to "talk relay," I really just needed to configure a few buttons (in the `yaml`):

```yaml
garage_door_1:
  name: Garage Door 1
  icon: mdi:garage-variant

garage_door_2:
  name: Garage Door 2
  icon: mdi:garage-variant
```

And some automation scripts to tie it all together:

```yaml
####################################################
# Garage Door Triggers
####################################################
- id: garage_door_1_trigger
  alias: Trigger Garage Door 1
  description: ''
  trigger:
  - platform: state
    entity_id:
      - input_button.garage_door_1
  action:
  - service: mqtt.publish
    data:
      topic: "ctrl/stanley/lab/garage/door"
      payload: "1"
  mode: queued
- id: garage_door_2_trigger
  alias: Trigger Garage Door 2
  description: ''
  trigger:
  - platform: state
    entity_id:
      - input_button.garage_door_2
  action:
  - service: mqtt.publish
    data:
      topic: "ctrl/stanley/lab/garage/door"
      payload: "2"
  mode: queued
```

---

So that's it, all 3 protocols to make some garage doors work. So, I guess that's not really *too bad*, but it was more than I'd originally planned. Hah!

Still fun, and **WONDERFUL** to have the garage doors tied into my home automation system. Having that control really has been terrific. Have a gander at the gallery
of pictures from the project. There aren't too many, but maybe it'll give you a sense of the project, and inspire you to go do something cool!

[Garage Automation with SEL Protocol Album](https://immich.stanleysolutionsnw.com/share/YgHn0kfhbethMOSJ3ke8QODAm0hkEevMiA7NHYcWOz1S46gh95DBbQLWo8JC7mRBuI0)

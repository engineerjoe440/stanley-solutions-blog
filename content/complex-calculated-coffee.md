Title: Complex, Calculated Coffee!
Date: 2025-05-09 07:36
Modified: 2025-05-09 07:36
Tags: coffee, coffee-maker, control, controller, digital-logic, logic, plc, programming, relay, iot, selogic
Category: education
Slug: complex-calculated-coffee
Authors: Joe Stanley
Summary: Admit it, you've always wanted an overly-complex coffee-making machine, haven't you? Something that's innately simple to use, but a complex masterpiece to marvel at; especially on those early Saturday mornings when the caffeine hasn't kicked in yet. Well, I've done it. I've built just that. I call it... the 5282. Let me explain.

This little endeavor started as a joke. No kidding. I'm not going to tell the whole story here, but if you ask nicely enough, I might tell you in person.
If you know, you know...

I wanted to make a single-cup coffee maker that runs off of an [SEL-2411](https://selinc.com/products/2411). The SEL-2411 can use digital or analog inputs to
interpret the various sensors, and it has a variety of output mechanisms which may be used to do all sorts of fun things with controlling the coffee-maker.

In one of my last days of teaching ECE101 at the University of Idaho, I brought in my 2411 to class so that I could collaborate with the students to design
the digital logic circuit required to operate the controller. We started with a simple control for the LED and pump motor, but after some further setup, I
realized it was going to be a bit more complex. Not unwieldy, but certainly more than we'd accomplished in class. What follows is the complete logic.

<img src="{attach}/images/SEL-5282.drawio.svg" style="width: 100%;" alt="digital logic for the complete controller">

Of course... this is very way over-complicated. But hey... We do this stuff because it's fun and interesting. And we learn something new with each new project.

This particular system was fun for me to learn about the particular design that was used in the coffee machine I disassembled to accomplish my goal. There was
a lot more sensing involved than I originally expected. In total, the I/O list was as follows:

- *2x* Thermistors (likely around 50kΩ nominal according to my research -- not tested, yet)
- *1x* capacitive water sensor
- *1x* rotary encoder
- *1x* 12V solenoid valve
- *1x* 12V pump motor
- *1x* 120V heater element

That's all quite a bit of sensing and closed-loop control design to put together. So I just decided I wasn't going to do any of that. I opted to simply use an
open-loop control mode based purely on timing. I suspect that the original system really just used the sensing to increase or decrease the motor speed in
order to manipulate the residence time. The residence time is, of course, the time which the water would spend in the heating apparatus (a metal tube with the
heating element running through it). The longer the water remains in the heater; the hotter it gets! Simple, isn't it?

Well, my design took a *different* approach. That's right. I took the approach of just turning the pump on "full blast." Who needs temperature adjustments, anyway?
That did result in my inability to achieve *quite* the same temperatures that the original coffee machine controls achieved. But I got close enough. In fact, if
you look closely at the output controls (enlarged below to highlight some of the important details), you'll notice that there's actually a timing system for
pulsing one of the outputs in a 4-seconds-on, 1-second-off pattern; that's an 80% duty cycle for a 5-second periodic signal. I used this to control the solenoid
valve which is used to switch between pumping water into the single-use-pod to a recirculating system. Using that recirculation on a cycle allows me to heat up
the water just a little more. Just what we needed!

<img src="{attach}/images/SEL-5282_timing.drawio.svg" style="width: 100%;" alt="output control timing">

Now, that's all well-and-good, but a big part of this is also working out the LED and user-interfacing bit. This coffee maker won't be very good if I can't use
it to actually inform a user whether it's set for small, medium, or large (8, 10, or 12oz). This whole user-interfacing bit was where I actually had some
students work with me in class (I quite enjoyed this bit, actually). In class, we established what the goal for the LEDs and push-buttons were going to be, then,
using the digital logic principles we'd worked on through the semester, we designed the circuit.

<img src="{attach}/images/SEL-5282_ui.drawio.svg" style="width: 100%;" alt="user interface control">

Worth noting is that this logic design is slightly modified from what we designed in the class, but that's really because I changed my mind when the LED should
blink versus being solid. I wanted blinking to indicate to the user they may change the setting (for small/medium/large); and I wanted the solid LED to indicate
which selection had been made.

---

Well, that's probably enough for now. If I'm feeling ambitious later, I might just post the settings here, too. But for now, have a great summer!

<iframe src='https://immich.stanleysolutionsnw.com/share/AQfx1LH7oW4xQEWuB2iHjRdmJsV2s4TZjJoTXKlKnk6Y5qIl0ovMlgZZ4W6HFF21sIc'
width='100%' height='600px' frameborder='0'>
</iframe>

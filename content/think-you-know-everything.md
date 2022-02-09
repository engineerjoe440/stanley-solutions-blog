Title: Think you Know Everything?
Date: 2022-02-08 19:50
Modified: 2022-02-09 07:54
Tags: Analog, Logic, 4-H, Knowledge, Throwback
Category: Youth
Slug: think-you-know-everything
Authors: Joe Stanley
Summary: A step back down memory-lane, I pulled out the ol' 'Quiz Board' for a presentation!
Gallery: {photo}quiz-board


This is gonna be a quick one, but I just wanted to share some photos of my old high-school
engineering project, the ***"Quiz Board"***. It was a project of mine to make a *cool*
and engaging public education system. I used it at the county fair to help teach folks about
swine, since that was my 4-H project.

<img src="{attach}/images/quiz-board/22-02-08 17-02-31 1227.jpg" style="width: 40%" alt="The Quiz">

## The Inspiration

Long ago, in a town far away, I was given an old "quiz board" to fix. It was literally a board,
and it had screws protruding from both sides. The system was simple. There were questions printed
on the left side, answers printed on the right. If you connected the provided wires using connected
alligator clips the board would tell you if you were "right" by illuminating an little bulb.
Pretty neat little idea for kids, you connect a wire on the left to select the question, then you
can connect the wire on the right to select an answer. If you were right, the bulb lights up!

#### But it was boring!

Or at least, I thought it was. There was no *real* feedback from the system if you got the answer
wrong, and it was kinda sad, for that reason. Needless to say, I wasn't satisfied. It wasn't long
after I repaired that board before I was starting to mull over ideas of how I could make my own
and improve upon the design.

Around the same time, I was learning about how Walt Disney had used rotating "drums" with little
depressions to make practical control systems before precise timing in microcontrollers was easy
and practical. I distinctly remember an old clip from some archive of Walt giving a tour of some
of the Haunted Mansion Audio-Animatronic control systems, and showing how these big rotating drums
would depress and release valve controlls for the pneumatics. These valves would then, in turn,
operate the cylinders responsible for actually moving the animatronics around, and by coordinating
all of these depressions at just the right speed and timing, the Disney Imagineers could craft
some spectacular repeating animations. Wonderful!

I liked that idea, and I had NO idea how microcontrollers worked. I didn't even have an Arduino
yet, and I had never even seen real software code (needless to say, my parents were not the
biggest tech-geeks in the area). So I started mulling this over. After what must've been a few
months (really, I can't remember), an idea came to me. I realized that those little snap-action
switches have two positions, one defaulting to ON, the other defaulting to OFF; more commonly
referred to as "Normally Closed" and "Normally Open," respectively. That meant that I could use
two switches pretty easily to "route" electricity for a couple of buttons labeled "TRUE" and
"FALSE". The switch associated with the _right_ answer would be pressed, the other would not.
That meant that I could easily "line-up" the switches so that if the user pressed the _right_
button, it would turn on a green light, and if they pressed the wrong button, it would turn on
the red light.

Thus, "The Quiz" was born.

gallery::{photo}quiz-board

#### Processing with Electro-Mechanical Logic

I love touting that this machine had a 3-bit processor; which, if you stretch your imagination
a little bit, I guess that *is* true since it had three switches, and their positions all
mattered for the result of the question/answer. I've already explained what two of the switches
were for, but that third switch was responsible for keeping the whole thing moving in just the
right way. That's right, that last switch was responsible for controlling the motor.

The whole system revolved -pun intended- around this rotating drum idea. Questions were printed
on a sheet of paper taped to a 4" diameter piece of PVC pipe, and the pipe turned to line the
questions up with a "viewing window" in the face of this gargantuan machine. When the user
pressed "start" that would deactivate the "constant" source of power for the motor, so as soon
as the next switch press happens, the motor would stop. This would, in turn, line up the
question with the viewing window, and then the user could read and respond to the question.

This whole project took my father and I much of the year to build. In all, probably between one-
and two-hundred hours, total. When it was finally completed, I got to take the machine with me
to the Clearwater County fair, and load it up with questions about pigs to help entertain and
educate the public.

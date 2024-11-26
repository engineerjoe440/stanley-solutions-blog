Title: A Collaborative Word Cloud for Teaching
Date: 2024-11-26 10:35
Modified: 2024-11-26 10:35
Tags: python, react, teaching, youth, software, development, fastapi, material-ui
Category: development
Slug: a-collaborative-wordcloud-for-teaching
Authors: Joe Stanley
Summary: A few months ago I wrapped up some work on a fun little project I developed for some teaching exercises. Let me tell you about it!

It started back in June when I was frantically preparing some exercises to teach and prepare a group of the College Staff to support Idaho's
[State Teen Association Convention](https://www.uidaho.edu/extension/4h/events/stac). I was trying to prepare some training to align the team.
That's not something I've done before, and I can't make any claims that it's perfect, but I think it was well received.

Let me explain what that exercise really was...

I used a handful of different materials to try making it both fun and engaging. Some of those materials were from National 4-H's
["Meet Up Buddy"](https://www.4-h.org/wp-content/uploads/2024/04/09105552/4H-Harmony-Guide-2024.pdf) card activity. Some were of my own
creation to encourage the College Staff to think about how to prioritize things when time constraints pressed them. My alignment training
was where we started, it was basically a challenge to the participants. Here's how I set it up, though, maybe not in so many well-placed words.

> 4-H is full of projects. So many things for youth to engage with and to find their spark. While this is wonderful, it does pose a bit of a
> challenge. Before I explain, I want you to think about all the words that come to mind when you think of 4-H.

At this point, I'd share a QR code with them that they could use to navigate to the game page. The game page provides participants with a
text box where they can enter each word that they think about. When they enter a word, a new text box appears so they can enter another word.
As they'd enter words, my system keeps track of them (hidden, of course) and begins to create a word cloud with all of their entries.

When I decide that they've had enough time (normally it looks like they've run out of ideas for words), then I shut down the entry system and
reveal the word cloud generated from all of their entries. At the end of it all, we're left with something like this:

<img src="https://immich.stanleysolutionsnw.com/api/assets/5692b76b-9049-4ebc-b0b8-4812c751716a/thumbnail?size=preview&key=klMHZEmZIUXG5UF9NeiFfKmLCZOcCm99k9mdI6Rw_U9TbJhC6zepXq-tEantGNrj748" style="width: 100%;" alt="college staff word cloud">

That gives us something to talk about.

> Look at this. These are all the things that our little group thinks about when we think about 4-H. But what do we share?
>
> Often, we're working in our own little silos, not terribly focussed on the same things that other leaders are focussed on. That can make
> working with other leaders difficult. We're each moving in our own direction, and sometimes, that feels like pulling a ball of yarn from
> different ends; just making the knot perpetually tighter.
>
> But this shows us something. Even when we are moving in different directions, it's possible to find some common ground. These are the first
> things that *you* thought of when I asked you to think about 4-H. These are the inately tied to your path in 4-H, and see how we have
> something common shared between us?

At that point, I'd talk about why I think it's good to get a common understanding of what is shared between the group, and how I like to think
about using this commonality with people to find shared ground on certain topics. To move forward together on what we see as the shared pathway.

It worked pretty well for our little team, I was able to refer back to it a number of times, and it made working with the team all the more
pleasant and constructive.

---

The exercise wasn't purely without its challenges, however. In fact, we discovered that the web-service that I'd chosen to use only allowed
something like 10 players, and each player could only enter 15 words. Not exactly the sort of restrictions you want to run into during an
exercise. Add to that, the fact that you've got to have a solid internet connection, which is not always easy in 4-H programming in the state
of Idaho.

That's why I returned to my recent build, the [PortaServer](/making-portable-digital-learning.html). My little (not so little, actually) ammo
can with a stack of mini computers. I could serve my own system there, and since I run the network, I could also make the address very easy
to access.

> Enter: [WordWall](https://github.com/engineerjoe440/wordwall)

It's pretty simple in concept. A little more effort in practice, but that's alright. I made a Python FastAPI server with a tiny, ephemeral
SQLite database backing it to run all the management of adding, removing, and sharing words. Tie that with a Material-UI based React frontend,
and I've got a relatively simple little service that I can run on my own system.

Now, I've got something I can take with me, wherever I travel to align 4-H leaders, youth, or others.

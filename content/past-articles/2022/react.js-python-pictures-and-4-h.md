Title: React.js, Python, Pictures, and 4-H!
Date: 2022-01-26 17:35
Modified: 2022-01-26 17:35
Tags: python, react.js, 4-h, fastapi, materialui, linode
Category: Youth
Slug: reactjs-python-pictures-and-4h
Authors: Joe Stanley
Summary: How do you get nearly one-hundred high-school age youth to collect nearly as many photos for a competition at a youth conference? Facebook? Google-Drive? How about Python...?


Do you remember going to those youth conferences when you were younger?

I do!

I loved them!

In Idaho 4-H, there's an annual conference known as the
["State Teen Association Convention,"](https://www.uidaho.edu/extension/4h/events/stac) though, admittedly,
when I attended, it was known as "Teen Conference." Essentially, it's a conference focused on giving youth from
around the state the opportunity to explore what opportunities exist after high school. Youth get to spend about
four days on campus at the University of Idaho, and explore various career- and education-focused "tracks."

But what would a youth-conference be, without some social activities and competition?

Idaho "STAC" has a number of social activities and competitions in addition to the educational portions to help
bring youth across the state together and help them build new connections. One of the competitions that happens
throughout the conference is what's known as "district competitions."

### What are the districts, and what are the district competitions?

Well, the state of Idaho is broken into four regional districts: Northern, Southern, Central, and Eastern. The
districts help keep some organization across the state, and at STAC, they are the dividing line(s) for youth
meetings.

Throughout the conference the districts compete against one another for points in district competitions. After
all, who doesn't like a little good-humored, friendly competition? Now, to be honest, I don't think that there's
any specific "prize" to come out of winning, but it's a lot of fun.

There are competitions focusing in a few key areas including creativity (photo contest, skit performances) and
healthy living (skit/dance performances).

### The challenge...

The photo competition is always an interesting challenge to host. It ends up becoming something of a technical
challenge to administer since there's no "effective" way to collect the photos into one place. In years past
all forms of systems have been used; everything from Facebook with hashtags, to public Google Drives, email, and
more... It's been a pain!

Last year something dawned on me, we could create something a little more interesting!

What if we created a simple little web-app to allow the youth to upload the photos they take for the competition,
and made it a requirement for the youth to agree to a photo-consent-release. So that's what we got started on!

### The Solution:

I spent some time a few months back doing some research on what we could use for an effective photo storage system.
I wanted to use an open-source project that would allow API-based access to upload photos, and whose management
is simple, intuitive, and without too many frills. I did some poking around, and playing with different services
on a $5/month Linode (love those things for testing, by-the-way), and I finally landed on
[Lychee](https://lycheeorg.github.io/) for a couple of reasons:

* There's a terrific, and simple `docker-compose` configuration provided by [LinuxServer.io](https://docs.linuxserver.io/images/docker-lychee)
* The API is VERY WELL documented, and exceedingly simple
* There's already a [Python Lychee client](https://pypi.org/project/pychee/)
* The user interface is very simple and focused without too many frills

Using Lychee as the "back-end storage" for this project, I can create a nice "wrapper" on the front to make an easy
web-app to allow youth delegates to upload their photos. To do that, I can use my slick little Python/React.js
integrated web-server pairing.

*Want to see what it's looking like?*

<img src="{attach}/images/idaho4h-photo-upload/Screenshot_20220126_174318.png" style="width: 100%" alt="Idaho 4-H Photo Upload">

### Other Perks:

Pretty early on in this project's investigation, I met a 4-H'er who is actually learning about some programming, and
so we've been working together on developing the web-front-end interface for youth.

I've got quite a bit more fun stories to tell about how we're using my GitLab and Jenkins instances to help us keep
this project moving, but that will be coming a little later. That said, take a look at the consent form that we've built,
and the dark-mode that we were able to build!

<img src="{attach}/images/idaho4h-photo-upload/Screenshot_20220126_174254.png" style="width: 100%" alt="Idaho 4-H Photo Upload">

<img src="{attach}/images/idaho4h-photo-upload/Screenshot_20220126_174342.png" style="width: 100%" alt="Idaho 4-H Photo Upload">


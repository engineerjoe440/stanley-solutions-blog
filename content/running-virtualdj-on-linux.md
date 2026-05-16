Title: Running VirtualDJ on Linux
Date: 2026-05-11 15:56
Modified: 2026-05-11 15:56
Tags: audio, dj, dj-software, linux, software, virtualdj
Category: Linux
Slug: running-virtualdj-on-linux
Authors: Joe Stanley
Summary: I'm a Linux fan. There's no doubt about that. I've gone so far as to run Virtual DJ software for my mobile DJ work. I use Virtual DJ; I have since I used a free version with my first DJ controller, so I still use it now on Linux.

Audio on Linux continues to get better and better. And many of us who follow Linux or gaming developments are familiar with
the fact that systems are getting more comprehensive for running Windows software on Linux.

I've been a mobile DJ for a few years now. My first gig was back in 2014. Funny, now, how that's more than 10 years ago, and I was
worried that I wouldn't get enough clients... Anyway...

I picked up a Numark Mixtrack II controller pretty early on. That controller set me down a path. Before that, I'd used MIXXX to
play music and allow me to run two decks and do the basics. MIXXX works on Windows, Mac, and Linux, and at the time, I was just
running on my Windows laptop. At the time, I would occasionally encounter a software crash, or some other issues. So when I
started getting the controller working, I started exploring the "Virtual DJ" software that was included, free, with the controller.
Turns out, I really came to like the software, and I started getting powered up with the new software. I ended up purchasing the
Virtual DJ 8 version for my controller.

Now.. a couple years back, I decided to switch over to Linux as my primary setup. I chose to use Kubuntu to give me the best of both
worlds... Total Kustomization (miss-spelling intentional), Kontrol, and well... the stability of Ubuntu.

It was around this time that I needed to jump in to DJ a youth event when I didn't have any of my own equipment with me. I barely
had my old laptop to have access to my music. At that time, I'd just started playing around with [Bottles](https://usebottles.com/)
which makes working with [Wine](https://www.winehq.org/) on Linux super easy. At that time, I'd tried loading Virtual DJ's 32-bit
build, and found that it was moderately successful. To add to this, there's nothing like a deadline to make things happen. So, time
to try things out. I was nervous that things might not work, but I was the "backup DJ", anyway, so I felt like any issues I might
have would probably be forgiven.

Turns out, the whole thing worked pretty well! Later that year, I went for a new laptop, and it's been working even better ever
since! This was all back in 2022, so I've been using this setup for 4 years, now. I've been pretty happy.

---

So what's needed to get this whole thing set up, anyway?

1. Install [Bottles](https://usebottles.com/)
2. Set up a Bottle (wine environment) for Virtual DJ to run within. The bottle specifics really aren't too specific from my testing. But I found that the Soda 9.0.1 runner works well.
3. Download the 32-bit Virtual DJ installer from here:
4. Run the installer in your new Bottle.
5. Create a link to your music source so that it can all be easily explored from the comfort of your VirtualDJ software. See the following command that I use.

```bash
ln -s /data/OneDrive/Audio/ /home/joe/.var/app/com.usebottles.bottles/data/bottles/bottles/VirtualDJ/drive_c/users/joe/Desktop/
```

> ℹ️ **Obvious Information** This command is tailored to my particular installation. It's probably not something that will work
> directly on your system. You'll need to modify a couple things:
> 
> - `joe` My system username. You'll need to swap that out.
> - `VirtualDJ` The name of the specific Bottle for which the folder link should be made.

---

I have had a few issues with this setup. The main issue I've run into is that occasionally, after a Bottles upgrade, some issues
appear where I can't launch the Virtual DJ app, anymore. The solution is always to blow away the Bottle (delete it), and
re-install it.

The other issue is that the files are not always easily accessed. So sometimes that requires a little tweaking.

---

I've really enjoyed this setup, even if it gives me a little gruff every once in a while. But I wouldn't encourage a first-time
Linux user to set this up without really trying things out, first.

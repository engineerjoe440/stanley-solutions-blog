Title: Why do I Self-Host?
Date: 2021-09-28 21:53
Modified: 2021-09-28 21:53
Tags: self-hosting, servers, computing, hosting, web, services
Category: DevOps
Slug: why-do-i-selfhost
Authors: Joe Stanley
Summary: I was recently asked "why do you run your own servers, when there's perfectly good, cheap, cloud providers?" Well... Here's why!


I was recently having a conversation with a few techie friends about the ridiculous and nerdy things that I'm doing at home. And, yes,
I realize I'm very nerdy. If that isn't clear already, go read some of my other articles.

One of my friends was curious why, exactly, I've decided to self-host so many of my services when I could easily lob those things up on
some cloud-service like [Linode](https://www.linode.com/unplugged). It's a fair question! To my friend's point, those services are fast,
easy, and require very little maintenance (comparatively, of course). To be clear, I mean that these services manage much of the storage,
hardware constraints, and networking limitations that I'm working through regularly. There's still the regular work of updating operating
systems that needs to be managed whether the server is running locally or in the cloud.

I won't discredit these features! They're quite attractive, but there's still reason for me to keep my servers plugged in.

*Let me explain...*

### Reduce, Reuse, Recycle

This point is perhaps the most important to me. I believe I've mentioned before that a lot... Let me emphasize that point...

***A LOT***

of the hardware I'm using is old. Many of the computers are what could be considered "ancient" desktop towers. They're old computers doing
modern things. In fact, at this point I think I have more 32-bit computers than I do 64-bit ones. Before you ask, yes, it's a bit painful;
but it's worthwhile. I mean, just think about it... I'm currently running seven computers that other people were ready to just throw in
the trash. That's 7 computers that didn't need to be recycled, 7 computers whose lifetime just got extended courtesy of yours truly.

Admittedly, they're power-hungry, and they're not as powerful as more modern equivalents, but they're doing great things for me, and that's
something that they wouldn't be able to do otherwise. Others would more than likely just chuck them, and I think it's far more valuable to
milk those old machines for everything I can. Perhaps it's just the naive part of my personality, but I'd like to think that these little
choices have an impact in some small way.

### My Disks, My Data

As just about any self-hosting fiend would likely tell you: "my data lives on *my* disks". Point being, since I own the disks, I'm the
proprietor of the data, too! That means I don't ever have to concern myself with whether or not I can revoke control over the data. Now,
I'll grant, this certainly makes me sound a bit more like a conspiracy theorist or an "old codger". I guess I don't have any rebuttal
against that. I'll just have to take it.

#### Data that's Important to Me, For My Eyes Only

To tack on to the previous point, since I own the data, I can use what I consider "private" or "privileged" data on my servers. Why?
Because I own them! I can *see* where the disks that store the data reside. Now, I know this may not seem like the greatest argument, but
when it comes to the argument of security and sensitivity, isn't it really all about perception and comfort anyway?

To put it another way, why do millions of homeowners install a home-security system? Is it because they think that the system will
immediately stop thieves in the act? Wouldn't better deadbolts and barred windows provide the same level of protection? Perhaps,
but then, maybe not. I'd expect that in more cases than not, homeowners want a balance. They want features, and they want function.
They want to *feel* secure, and they want to enjoy their home without barred windows and dozens of deadbolts.

That's why having my "private" data on my local servers is important to me. I've been graciously granted numerous data-set samples to
test some of my other Python projects against, but that data is important to the people who gave it to me. It's the sort of data that I'm
honored to have been granted access to, and I don't really think it's appropriate to share with the rest of the world. So, I host it on
servers that live in my basement. Somewhere that lives behind *my* firewalls.

I don't think that my solution is right for everyone, and I don't think it's the "be-all-end-all" solution that I wish it was, but it
works for me, and makes me happy! After all, if it helps me sleep well at night, isn't that worth something?

### Diversified Service Structure

You've heard of diversified investments, haven't you?

Well, that's kinda what I'm doing with my diversified infrastructure. You see, I'm not *only* self-hosting. <gasp!> I'm also using cloud
services (namely Linode - thanks, Linode Team!) to help me with some services, and I'm planning to spin up some others in the (relatively)
near future. Sometimes speed is important, sometimes it's not. When speed *is* a concern, I try to host on Linode, since they're so
**SUPER-FAST** and available, it makes sense for me. But in other cases, it doesn't make sense.

That's all part of the whole "multi-cloud" paradigm anyway, though. Different providers for different applications, diversified to be more
robust. In fact, I *do* use Linode for some off-site backups. I'm still working out my backup strategy. It's not the greatest, at the
moment, but it's coming along, and some of that is thanks to Linode's services, and the peace-of-mind they offer. Mind you, the data I'm
backing up to Linode still goes through secure tunnels, and it's not the "private" data that I was mentioning earlier.

### Hands-On Learning Opportunities

My last point for keeping these machines kicking around in my closets, basement, and elsewhere is because they all offer me some great
opportunities to learn! After all, if I'm going to keep these things up and running, I've got to constantly be improving, adding, reworking
and modifying to (stealing a bit from my 4-H background here) make the best better. Having these servers in my house affords me the ability
to simply plug in a USB stick, or connect a monitor if I blow up SSH so badly I can't reconnect. It means that when I botch the install, I
just start over, and when I need to copy the whole darn disk, I just pull it out and stick it in my external hard-drive bay.

Believe me, I've learned a lot in the past year playing with these things and keeping them up. And there's still a lot more I want to learn.

-----

So that's my story, and I'm sticking to it.

Like I mentioned earlier, I wouldn't recommend this to everyone; it's a solution that fits my needs, but that may be different than what
others are interested in. Still, I'm proud of the fact that I'm running so much out of my own home, and I'm excited to keep growing with
these old computers. I'm happy that I'm able to reuse machines that would otherwise litter some landfill, and keep things running for
myself and some of the university students that I support.

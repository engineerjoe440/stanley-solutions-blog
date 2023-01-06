CI/CD On Industrial Grade Hardware
##################################

:date: 2021-02-07 16:19
:modified: 2021-02-07 16:19
:tags: SEL, Industrial, Rugged Computer, Ci/Cd, Development, Server
:category: DevOps
:slug: jenkins-on-sel-industrial-hardware
:authors: Joe Stanley
:summary: Run DevOps CI/CD pipelines on industrial equipment with no moving parts? Ok! Sign me up!!!


Yes... I already have too many computers. But with that said, what's a few more?

I know it was only about a month-and-a-half ago that I was writing about Jenkins
running on a Raspberry Pi, but I outgrew that pretty quickly. In reality, I
really just started with it, and basically gave up; but hey! I learned a lot in
that time. So now, I'm upgrading!

The new hardware
----------------

I am something of a hardware graveyard. Old machines come to me to live out the
end of their lives and, eventually, give up the ghost. I managed to get my hands
on some second-hand industrial computers, to do some bidding for me. Namely, I
picked up some old SEL (Schweitzer Engineering Laboratories) SEL-1102 rugged
computers. They're based on an old Intel x686 processor, and don't have anything
special in the memory arena... but they're super solid machines.

.. image:: {attach}/images/SEL1102/IMG_0849.jpg
   :alt: SEL Rugged Computers to Run my DevOps Pipeline
   :width: 600 px

My comment about being a "computer graveyard" might still apply to these
computers too, but well, they've got a lot more life left in them. You see,
these are ruggedized computers designed for installation into some of the most
extreme environments around the world. Rated for harsh operating conditions,
built with no moving parts (that's right, a computer without fans), and a whole
slew of serial ports (16 DB9 ports alone). SEL maintains a 10 worldwide warranty
too; but I'll grant that this warranty is void because these devices were sold
to me secondhand. I bring up this point, however because it really exemplifies
the commitment to quality that SEL brings to the table.

Now, for those of you who know me well, you'll also know that I *work* for SEL.
So yeah, I do have some bias there; but I've also gotten to see (first-hand) the
quality that we at SEL put into our products, so I'm very proud to have a few of
these machines running at home, and I'm very excited to put them into production.

The new work
------------

With these new servers, I'm excited to set them up running Debian (because, yeah,
they will do that - and very well, I might add) to support a Jenkins server. I
plan to use that, and expose it as my primary integration system. With Jenkins
running on these new machines, I'm going to set up a Pi Cluster to offload the
actual pipeline work.

But why?

Well, I want the main Jenkins server to be just that... the main server. I want
other machines to do all the "dirty work" for me.

So, before you get too carried away with your thoughts; yes, that does mean more
computers. I've already put in an order for a Raspberry Pi cluster, which I'm
very excited about; but that's another article for the near future.

Part of this excitement also stems from my need to integrate with some SEL relays
serially for testing with my SELProtoPy project. With all of those serial ports
on these computers, I'll be able to tie in to those relays quite nicely to allow
some really solid automated testing. Better yet, with all of that integration,
I'll be able to do some really nice pipelined builds for testing SELProtoPy and
PyCEV.

What's next?
------------

Well, next on my plate is to get these machines up and running on my network so
that I can access them remotely and start integrating with GitHub actions to
fire off the builds and testing.

I'm very excited to be putting some SEL equipment to work in my own personal
development practices, so I'm sure I'll have some more updates as I go along!

.. image:: {attach}/images/SEL1102/IMG_0850.jpg
   :alt: Putting some SEL Hardware to Work
   :width: 600 px


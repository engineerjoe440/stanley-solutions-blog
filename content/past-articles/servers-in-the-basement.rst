Servers in the Basement...
##########################

:date: 2021-02-14 19:23
:modified: 2021-02-14 20:40
:tags: SEL, CI/CD, Jenkins, Dev-Ops
:category: DevOps
:slug: jenkins-servers-in-the-basement
:authors: Joe Stanley
:summary: Some people keep their creepy Christmas decorations in their basement. Others keep their continuous integration servers down there too...


.. _selprotopy: https://github.com/engineerjoe440/selprotopy
.. _pycev: https://github.com/engineerjoe440/pycev

.. image:: {attach}/images/jenkinsbasement/IMG_0851.jpg
   :alt: SEL Rugged Computers mounted and ready for work!
   :width: 600 px

Whelp, I've gone and done it. I've mounted and installed one of my SEL computers
and set it up for running Jenkins!

This isn't going to be a very in-depth article, but I wanted to say that it's
done. The server is mounted with a brand new switch and surge protector (no UPS
for the moment, but perhaps to come in the *relatively* near future). They're
networked back upstairs to my little IT closet, and Jenkins is waiting idly for
me to push new code.

I spent Saturday mounting the server, re-routing all the networking, and setting
up my modem to provide access to the servers by way of a reverse proxy. Perhaps
I'll document what that is and how it works, but that might be another article.

Today I got to work standing up a few `pytest` projects for both `selprotopy`_
and `pycev`_, what's exciting about this though, is the fact that they're set up
now so that they can access the private resources they need for testing, but
they can be kicked off by my commits and pushes to their repositories on GitHub.

So... now I can really start cranking on that code, and Jenkins can do some of
my dirty work to start running the tests for me!

.. image:: {attach}/images/jenkinsbasement/IMG_0852.jpg
   :alt: Gotta love that SEL blue!
   :width: 600 px

I want to restate that I'm very excited to be using some old SEL hardware and
giving it a second lease on life. These computers are rugged, industrial
machines; and I'm getting to put them to work making these projects solid. Not
to mention that these projects are actually tailored to supporting SEL tech.

Yep. It's nerdy.

Yep. I'm still excited.

Yep. You guessed it; I'll surely be giving more updates moving forward!
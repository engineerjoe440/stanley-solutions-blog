`pycev` - A Python CEV Reader
#############################

:date: 2020-12-12 10:59
:modified: 2020-12-12 10:59
:tags: Python, SEL, CEV, Event, Record, Files, Power System, Analysis
:category: Python
:slug: pycev-a-python-cev-reader
:authors: Joe Stanley
:summary: Another new project? Well, why not? This time, we'll be tackling reading CEV files from SEL in Python.


.. image:: https://raw.githubusercontent.com/engineerjoe440/pycev/main/logo/pycev.png
   :alt: Introducing: pycev!
   :width: 600 px

Wait...

Another new project?

Yes. That's right. I'm starting another new project. But hey! There's a lot of framework
that needs to be introduced before I can start doing all the cool high-level stuff that we
all want to see and use. I mean, by now you should understand that I'm all about getting
the framework right. If you're still not sure, go read my rant about getting the framework
right... `This is my rant on getting framework right. <https://blog.stanleysolutionsnw.com/write-framework-once.html>`_

Goal:
-----

So what's the plan here, anyway?

Well, this project, `pycev` (I've almost considered that it should be pronounced "pie-safe", but
that's not how it looks, so we'll let that stew a while longer) will be a package for reading and
interpreting SEL Compressed EVent records. They're a proprietary (but open) format in which SEL
protective relays collect event information and "compress" it into a format that's easily read
by machines (computers).

There's already a handful of projects out in the wild for reading COMTRADE records; which, if
you're unfamiliar are "*Common Format for Transient Data Exchange*" files, and are supported by
many SEL relays in addition to a much broader number of other vendor devices. Trouble is, not
everyone uses COMTRADE, and comparatively, CEV files are a little simpler, and (in my opinion)
more straight-forward and robust. Perhaps the best Python project for reading COMTRADE files
is `Python Comtrade`_. That project shows great maturity and value. It also sees regular updates
and bugfixes as needed.

.. _Python Comtrade: https://github.com/dparrini/python-comtrade

Since it's such a well respected and mature project, I'd like to take it as inspiration for
`pycev` and use it to help me realize the best API for the package so that the two libraries
could (potentially) be used interchangeably for various projects.

What's First?
-------------

Well, I guess starting the package development is first!

I've already carved out a repository, and I've got something of a skeleton package put together.
I think the first step will be getting enough working that I can upload it to PyPI to reserve
the namespace. Then full development will need to come. There's a good handful of things that
need to be tackled:

- Upload Project to PyPI
- Develop Core Functionality and Match API to that of "Python-Comtrade"
- Develop Automated Test Suite with Local Server and Various Existing CEV Files

So that's the sort of roadmap I see before me. Now, the time-frame is still way up in the air;
so who knows whe this all will *actually* happen. But here's hoping!

If you're interested in checking in on the project, and would like to jump in and contribute,
have a little look at the `repository`_, and feel free to open an `issue`_ to start a conversation!

.. _repository: https://github.com/engineerjoe440/pycev
.. _issue: https://github.com/engineerjoe440/pycev/issues
Title: Using Python to Provide Simple Photo Connections for Youth
Date: 2022-02-13 20:44
Modified: 2022-02-15 20:17
Tags: Python, React.Js, Microservice, Docker, Lychee, Youth, Development, Fastapi
Category: Youth
Slug: using-python-to-provide-simple-photo-connections-for-youth
Authors: Joe Stanley
Summary: So if you're gonna use Python to help bring photos from youth together; how, exactly, do you do it? This article will look at how we're using Lychee, Python, FastAPI, and React.js to make an ultra-simple, highly effective photo upload service for a youth conference.

If you've been keeping tabs on what I've been up to lately, you might know that I've been slowly getting back into 4-H
involvement. Namely, I'm now a certified volunteer in Idaho, and I'm starting to dip my toes into leading projects.

Recently, I shared [how I'm working with youth to create an app in Python and React.js](/reactjs-python-pictures-and-4h.html)
and how I'm excited to be working *with* some of the youth to develop the app. We're working to use some of the "latest and
greatest" technology to ensure that the service is not only forward-looking, but helps to teach forward-looking practices.

In this article though, I want to talk a bit more about the technical details about what we're doing, and how it's working.

---

### Let's talk program organization...

The whole program is structured around Lychee as the "database". Since Lychee provides a beautiful, functional API,
and an easily maintained container-based database and storage, we can use it as the core of the service. Lychee
provides simple, but powerful album organization, and that's all available through the API (excellent!!!). Since
the entire goal is to provide a simple way to organize photos according to the "district" that submits them, we'll
be able to use the API to poke those photos into just the right spot.

It'll be the responsibility of our Python back-end (using [`pychee`](https://pypi.org/project/pychee/)) to make the
connection between the React front-end and the Lychee service itself. This same Python back-end will serve the
React public files. Effectively, like so many other places I use Python, it acts as the all-important glue in this
system.

::uml:: format="svg" alt="Idaho 4-H Photos Site" title="Idaho 4-H Photos Site" width="300px" height="300px"
   !theme spacelab
    skinparam actorStyle awesome
    actor User
    node NGINX {
        node Python-App as py{
            [FastAPI] as fastapi
            [React.js] as react
        }
        node Lychee-App as lyc{
            database DB
            [API] as api
        }
    }
    User --> lyc
    User --> py
    react <--> fastapi
    fastapi -> api
    api <--> DB
::end-uml::

The React front end is basically passive in this configuration, by that, I mean there's no Javascript/Node.js
server configuration on the box. It's all built and exported to static files that Python serves as needed to
"pull up" the site. Once the site is loaded, the React.js front-end just hits the appropriate API endpoints on
the Python side which, in turn, causes the Python service to access the appropriate API endpoints on the Lychee
service using a specific API credential-set.

----

There's a lot more going on in the automated build system that helps me work with youth to deploy the site in
the various stages of development so that the youth don't have to learn all of the intricacies of Node.js'
awful dependency stack. That said, I'll have to write more (hopefully soon) on how we tied my personal Jenkins
service with the Linode that this system is running on.

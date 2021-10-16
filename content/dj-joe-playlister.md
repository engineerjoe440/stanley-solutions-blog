Title: DJ Joe Playlister
Date: 2021-10-16 12:03
Modified: 2021-10-16 12:03
Tags: Spotify, Apple-Music, Python, Web-Apps, DJ, Docker
Category: Python
Slug: dj-joe-playlister
Authors: Joe Stanley
Summary: I've been going a bit crazy with the web-app craze lately. Let me show you what I've been up to...


I've been working up a fever on web-apps recently. Ones that I'm developing, ones that I'm deploying, and ones that
I'm reviewing. That goes for both work and home. Gosh... I think I need a vacation. Maybe next lifetime.

Recently, at home, my focus has been on several "DJ Joe Services," things that I can utilize for my mobile DJ work and
that will help me make those processes easier. Remember, I'm lazy! I want to find the easiest way to do things. Right
now, I've got two apps deployed, and I'll be working on a third here pretty soon.

The first app was an availability calendar. I'll have to write about it soon, since it was a fun project tying APIs,
Python, and React.js all into one solution. However, this is about my second app. What I call a "playlister," i.e.,
something that can slurp the playlist information out of another file/service/etc., and provide it in a more consumable
manner. Right now, it's focus is on Spotify and Apple-Music, since those are the two prominent sources that are
consistent enough for me to work with.

<img src="{attach}/images/Screenshot_20211016_120952.png" style="width: 100%;" alt="DJ Joe Playlister">

### Inspiration
As a mobile DJ, I often am provided "playlists" in various forms: Word documents, text
files, quickly-scribbled hand-written notes, Spotify playlists, and Apple Music playlists.

It quickly became apparent for me, that I spent *way* more time working through these
Spotify playlists and Apple Music playlists to get them into a form that was actually
helpful for me. In most cases, I could not simply copy/paste the Spotify list(s) out so
that I could search for the songs of interest in my own library and then determine whether
I'd need to aqcuire additional music. Thus... I came to the conclusion, I'd want a little
assistance from my computer.

### Stages of Development
I originally started with a simple Tkinter-app that used the [`spotipy`](https://spotipy.readthedocs.io/en/latest/)
package to pull playlist information into a simple plain-text file. It was helpful, but
ended up incurring a few additional challenges of its own. The largest of which being the
fact I had to securly pass the API secrets around with the script itself. This became a
real burden, so I decided to enhance the system into a full-service mini web-app that
could be utilized for exactly this purpose. The web-app could run persistently on a server
that could hang on to those secrets and allow me to access the tool from anywhere.

Thus, the `djjoeplaylister` was born.

### Technical Details
This app is built on the shoulders of giants, so let me give credit to those where it's due!

**Technology Specs**

* Language: Python 3
* Web Framework: [FastAPI](https://fastapi.tiangolo.com/)
* Web Listener/ASGI Server: [Uvicorn](https://uvicorn.org/)
* Reverse Proxy: [Nginx](https://nginx.com/)
* Hosting Provider: [Linode virtual hosting](https://linode.com/)
* Operating System: Ubuntu server
* App Deployment Enviromnent: Dockerized Container

**Python Packages Leveraged**

* Spotify Client: [`spotipy`](https://spotipy.readthedocs.io/en/latest/)
* Apple Music Client: [`requests`](https://docs.python-requests.org/en/latest/)
* HTML Table Generation: [`pandas`](https://pandas.pydata.org/)

Additionally, I'd like to provide a special thanks and shout-out to this gist that
helped me get up and running with consuming the Apple Music playlist without dealing
with Apple's crummy developer program ($99 dolars a year, just to access an API? No
thank you!)
[https://gist.github.com/aleclol/ef9e87d0964f00975f82d5373a814447](https://gist.github.com/aleclol/ef9e87d0964f00975f82d5373a814447)

------

That's it! My little DJ Playlister! Want to go see it? [Go Check it Out!](https://playlists.djjoeidaho.com/) It's not
anything too terribly special, and it's got plenty of room to grow, but it's a helpful little tool, and I think it
showcases the utility of the Python programming language.

##### I mean... just think about it.

I started with a simple little Tkinter script for which I had to lug secrets around all the time, and it was great! But
it had some significant shortcomings. Python to the rescue though, a little refactoring, and throw in some HTML, CSS,
and some more packages and I've got a full web-application. Still full Python, and it's fully-deployed! You can't do that
with a lot of other tools. Imagine if I had started with some Excel macro, or some bash script. It would've been very
difficult to scale those apps out to something that's actually useful in the context that I need.

***Not with Python!***

Preaching session over. Chat again soon, goodbye!

Title: Scraping the ISP Router to Support Self-Hosting
Date: 2022-08-26 16:27
Modified: 2022-08-26 16:27
Tags: self-hosting, isp, router, networks, ethernet, servers, networking
Category: Self-Hosting
Slug: scraping-the-isp-router-to-support-selfhosting
Authors: Joe Stanley
Summary: To host my home services, I need to be able to have a dynamic-DNS, and to do that, I've been using DuckDNS (a great service, by the way), but it's time that I start getting more serious, and remove theCNAME from my domain, and get something a little more proper. But... to do that, I'll need my public IP. Good thing my ISP-provided-router displays that on the front page! Now, it's time for just a little Python...


Routers have all kinds of "good stuff." A literal wealth of information, all we need is to tap that resource, right? That's just exactly what I'm working on.

See, I've started working on [a project](https://github.com/engineerjoe440/ZiplyFrontierRouterStats) to scrape all of those "goodies" from my Ziply (formerly
Frontier) router. All the important, and relevant stuff is provided right there, in the front of the user-interface. My little project is pretty simple, I'll
scrape all of the useful bits into a big dictionary, then getting any of that data is a cinch!

Python's already got all the horsepower that I need. I can use [`requests`](https://pypi.org/project/requests/) to pull the web-page down, and then use a
little [`beautifulsoup`](https://pypi.org/project/beautifulsoup4/) to parse everything into where I need it. Simple, right?

### *Exactly!*

Now, I've got my little tool all spun up so I can use it directly on the command line, but I can also use it to host a little web-server with
[`FastAPI`](https://fastapi.tiangolo.com/) and [`Uvicorn`](http://www.uvicorn.org/) to host a simple little app.

* Want to scrape the router statistics to your terminal? No Problem.
* Want to scrape the router statistics and serve them in an easily-consumed web API? You bet!!! Even easier!

I don't have much else to say about the little project. Probably won't ever release it on PyPI, but if people ever asked, I suppose that I could. If you
want to see it for yourself, go check it out on [my Github](https://github.com/engineerjoe440/ZiplyFrontierRouterStats).

## What's Next?

Well, I'm going to use this little tool, in conjunction with some Porkbun scripts to automate my DNS refreshes for my home-servers. This'll let me
bypass the reverse-DNS provided by DuckDNS (what I use right now), and let me get some better performance out of my system, as a whole! Namely,
I'll be able to change the CNAME records out for something a little more reliable for my home-server needs!

Leave a comment if you've got thoughts, questions, or just want to say hi!
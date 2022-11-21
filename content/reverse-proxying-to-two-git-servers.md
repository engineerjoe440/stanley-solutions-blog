Title: Reverse Proxying to two Git Servers
Date: 2022-11-21 13:54
Modified: 2022-11-21 13:54
Tags: Git, Self-Hosting, NGINX, GitLab, Gitea, SSH, Proxy
Category: Self-Hosting
Slug: reverse-proxying-to-two-git-servers
Authors: Joe Stanley
Summary: I'm quite the self-hosting fiend. That's well-established, at this point, but I wanted to go into some of the details about my recent adventures, exposing SSH service to both my GitLab and Gitea servers.

I host both a GitLab and Gitea server at home. I know, it's a bit wild that I've got two different Git servers at home, but it works to my advantage.
You see, I use GitLab for *most* of my development needs, and for the "center" of my infrastructure-as-code management. However, Gitea makes the introduction
to Git and development easier for some 4-H youth activities, so it's advantageous to keep around.

With these two servers running on separate machines, I need to have HTTPS and SSH tunneled through to both machines. With NGINX, that's not to terribly difficult for
the HTTPS services. NGINX does the HTTP reverse proxying, and Certbot comes in clutch to make the certificate stuff work nicely.

> Woah! Woah... Woah... What's a "reverse proxy?"

Glad you asked!

A reverse proxy is a way of *proxying* web requests through a single machine to multiple services on a LAN (Local Area Network). That is, if you're hosting lots of web-services
(like I am) behind a router, you can open the specific web ports (80 for HTTP, and 443 for HTTPS) such that internet traffic can access those ports on your proxy. From there, the proxy can determine where the trafic is destined (i.e., which server it needs to go to) and make the appropriate requests, funnelling all responses back to the user.

::uml:: format="svg" alt="Basics of a Reverse Web Proxy" title="Basics of a Proxy" width="20%"
   !theme hacker
    skinparam actorStyle awesome
    actor GitUser
    cloud WAN
    [Router] as router
    [Proxy] as proxy
    [Service1] as svc1
    [Service2] as svc2

    GitUser --> WAN
    WAN --> router
    router --> proxy
    proxy --> svc1
    proxy --> svc2
::end-uml::

---

## How's my HTTPS Proxy Configured?

Well, my specific system looks something like this...

::uml:: format="svg" alt="Stanley Solutions HTTP/HTTPS Proxy Configuration" title="Stanley Solutions Proxies" width="100%"
   !theme hacker
    skinparam actorStyle awesome
    actor GitUser
    cloud WAN

    GitUser --> WAN

    node Home-Network {
        portin Router80
        portin Router443

        node Gitea as gitea-srv{
            portin "80" as ge80
            portin "443" as ge443
            database Gitea
            component NGINX as genginx
        }
        node GitLab as gitlab-srv{
            portin "80" as gl80
            portin "443" as gl443
            database GitLab
            component NGINX as glnginx
        }
        node Reverse-Proxy as proxy{
            portin "80" as px80
            portin "443" as px443
            component NGINX as proxynginx
        }
    }
    WAN --> Router80
    WAN --> Router443
    Router80 --> px80
    Router443 --> px443

    px80 --> px443
    px443 --> proxynginx

    gl443  -l-> proxynginx
    proxynginx -l-> ge443

    gl80 --> gl443
    gl443 --> glnginx
    glnginx --> GitLab

    ge80 --> ge443
    ge443 --> genginx
    genginx --> Gitea
::end-uml::

## But, Joe, You Said Something about SSH?

Yep! That's right!

If you're not terribly familiar with Git, let me just say that you can clone either over HTTP(S) or SSH. In the following images, see how both GitLab and Gitea support
HTTPS and SSH:

<img src="{attach}/images/gitlab-clone.png" align="right" style="width: 30%; margin: 10%;" alt="GitLab Clone">
<img src="{attach}/images/giea-clone.png" align="left" style="width: 30%; margin: 10%;" alt="Gitea Clone">

<img src="{attach}/images/laughing-hysterically.gif" align="right" style="width: 20%" alt="Laughing Hysterically">

SSH is often just a bit faster, and brings other perks, but it can't be proxied in quite the same way as HTTP traffic. That's because SSH doesn't use hostnames in headers
in the way that HTTPS does. But, we can do some unique things to make some of this work to our liking.

## So, what DO we do, then?

In this case, we can customize the SSH services for both endpoints! We just need to use non-standard ports, and inform both GitLab and Gitea that they're using those
specific ports. That way when users clone repositories, the non-standard ports will be in the URL, and used automagically!
Title: Making Portable Digital Learning
Date: 2024-09-03 16:41
Modified: 2024-09-26 15:42
Tags: server, portable, learning, education, rpi, raspberry-pi, linux, open-source, gl.inet, python, nginx
Category: Self-Hosted
Slug: making-portable-digital-learning
Authors: Joe Stanley
Summary: With all of these 4-H activities that I've been helping with, I've been in my car. A lot. That means that I don't always have access to great internet, great resources, and I can't always connect home to my servers, there. I've decided to combat that by building a single, portable network. A network in a box, if you will. Here's how I did it.

That's right! I've been build a portable network and server system. It's all built into an ammo can. It's set up so that
I can drag around all kinds of services with me, and I can easily set up my own WiFi network for 4-H users to access.

Many of the locations I visit to support 4-H's hands-on-learning don't offer great networks, and in some cases, the
lesson(s) warrant use of some technology or service that requires accounts and special access. That puts all sorts of
undue challenges on me and others to put things together beforehand and waste some valuable time getting things working.

A few years ago (yes, it's been that long), I had an idea to put a few Raspberry Pi's and a little network switch in an
ammo can so that I could pack the whole thing around and use it for different programming/hacking exercises with 4-H
youth. That quickly evolved into what I now call the Port-A-Server. My portable network and server infrastructure in a
box!

This thing comes packed. Here's the BOM (discounting fasteners and cabling, of course).

| **Quantity** | **Device**                                                    |
|-------------:|---------------------------------------------------------------|
| 2            | Raspberry Pi 3B+                                              |
| 2            | Raspberry Pi 4B+                                              |
| 1            | Raspberry Pi CM4 in a Dual NIC Enclosure                      |
| 1            | ZimaBoard x86 Single Board Computer                           |
| 1            | gl.iNet Travel Router                                         |
| 3            | Small 1Gbps Network Switches                                  |

The whole thing runs off a single power supply which means ONE CABLE, and it's even got a couple power ports on the side.
Just a few months ago, I even ported through some ports to access the HDMI outputs from a couple of the crucial devices,
and USB for a bunch of things. With that gl.iNet router, I'm able to use its USB port to connect to my cellphone to use
cellular tethering. That means that in spots where WiFi isn't available, but cellular is, I'm set!

::uml:: format="svg" alt="Portable 'Network in a Box'" title="Porta-Network" width="100%"
!theme blueprint
!include https://raw.githubusercontent.com/plantuml-stdlib/gilbarbara-plantuml-sprites/master/sprites/raspberry-pi.puml
!include <osa/device_wireless_router/device_wireless_router-sprite>
sprite sbc <svg xmlns="http://www.w3.org/2000/svg" width="800" height="800" viewBox="0 0 24 24" fill="none" stroke="#020202" stroke-miterlimit="10" stroke-width="1.91" xmlns:v="https://vecta.io/nano"><path d="M22.5 19.66h-9.54l-1.92.95H1.5V4.39h21v15.27z"/><path d="M6.27 18.7v1.91M19.64 8.2h2.86m-2.86 3.82h2.86m-2.86 3.82h2.86M5.32 8.2h4.77v7.64H5.32zm8.59-.95v9.55"/></svg>

nwdiag {
  wan [shape = cloud]
  wifiUsers [shape = hexagon, description = <&person*4.5>]
  securedWifiUsers [shape = hexagon, description = <&people*4.5>]
  wan -- router
  wifiUsers -- unsecuredAP
  securedWifiUsers -- securedAP

  network 4-H_Mobile_Open {
      address = "192.168.9.x/24"

      unsecuredAP [description = "                <&wifi*4>\n 4-H Mobile (Unsecured)"];
      router [address = "192.168.9.1",  description = "<$device_wireless_router*0.25>\ngl.iNet"];

  }
  network 4-H_Mobile {
      address = "192.168.8.x/24";

      corePi [address = "192.168.8.2",  description = "<$raspberry-pi*0.5> CM4\n  CorePi"];
      corex86 [address = "192.168.8.3",  description = "   <$sbc*1.5>\n CoreX86"];
      pinode1 [address = "<DHCP Assigned>",  description = "<$raspberry-pi*0.5> 3B+\n Pi Node 1"];
      pinode2 [address = "<DHCP Assigned>",  description = "<$raspberry-pi*0.5> 3B+\n Pi Node 2"];
      pinode3 [address = "<DHCP Assigned>",  description = "<$raspberry-pi*0.5> 4B+\n Pi Node 3"];
      pinode4 [address = "<DHCP Assigned>",  description = "<$raspberry-pi*0.5> 4B+\n Pi Node 4"];
      router [address = "192.168.8.1",  description = "<$device_wireless_router*0.25>\ngl.iNet"];
      securedAP [description = "     <&wifi*4>\n 4-H Mobile"];
  }
}

  group {
    description = "PortaServer";
    color = "#ebebeb10";
    corePi;
    corex86;
    pinode1;
    pinode2;
    pinode3;
    pinode4;
    router;
    securedAP;
    unsecuredAP;
  }
::end-uml::

<iframe src='https://immich.stanleysolutionsnw.com/share/9yb9_5eOa4VWItFhjnzxuNnbU_7B63HkToT5a_Q5li4Oyy77o91bW0Gx6_hUbGITCYs'
width='100%' height='600px' frameborder='0'>
</iframe>

Now, this is all pretty slick, but what's a metal box full of computers without some kind of applications that they can
be used for? Good question! So how about we talk about the applications that are running on this system.

For starters, I'm running the venerable [PiHole](https://pi-hole.net/) for network-wide advertisement blocking, and some
small allowance of security. In addition to that, I'm using NGINX alongside the gl.iNet router to provide convenient
hostname access to the various applications. The CorePi device provides PiHole and NGINX services.

Beyond the networking applications, I also use a new Python-backed app that I've been building;
[WordWall](https://github.com/engineerjoe440/wordwall). WordWall is a pretty simple little application which drives a
collaborative word cloud application that I can use for some of the trainings I provide. As a matter of fact, I need to
share more about that training in a separate post.

> Someday... Someday...

Now, for a portable network, I really need some simple little file-sharing tool. So I've got that too! I'm using
[miniserve](https://github.com/svenstaro/miniserve) a simple little CLI application that I wrapped in a small `systemd`
unit file. That unit file helps make sure that the file system gets cleared before the application gets started, and
afterwards too. That makes it so any shared files are temporary only.

```systemd
[Unit]
Description=todo
```

I'm also going to be setting up a couple typing-games as little applications that some of the 4-H kids can play. I keep
hearing that kids aren't building great typing skills on their own. So... I aim to do what little I can to help work
that out.

Lastly, I'm also planning to set up a little self-hosted Kahoot alternative to use with quiz games for internet-deprived
classrooms. That application is [ClassQuiz](https://classquiz.de/), it's a pretty neat Python-backed application in its
own right. I really can't wait to start using it for some of my activities. I haven't fully wrapped up deploying this
application. It's going to require some SSL certificate management, but I need to figure some of that out. Hopefully
I'll be back to write more about that... later.

But this leaves me to question how I'm going to keep track of all my configuration files. Hmm... Well, I think that
calls for `git`, more specifically... [Gitea](https://about.gitea.com/) That ought to make my version control for these
little applications pretty slick-n-easy.

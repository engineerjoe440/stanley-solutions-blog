Title: Making Portable Digital Learning
Date: 2024-09-03 16:41
Modified: 2024-09-03 16:41
Tags: server, portable, learning, education, rpi, raspberry-pi, linux, open-source, gl.inet, python, nginx
Category: Self-Hosted
Slug: making-portable-digital-learning
Authors: Joe Stanley
Summary: With all of these 4-H activities that I've been helping with, I've been in my car. A lot. That means that I don't always have access to great internet, great resources, and I can't always connect home to my servers, there. I've decided to combat that by building a single, portable network. A network in a box, if you will. Here's how I did it.


That's right! I've been build a portable network and server system. It's all built into an ammo can. It's set up so that
I can drag around all kinds of services with me, and I can easily set up my own WiFi network for 4-H users to access.

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

### More to come...

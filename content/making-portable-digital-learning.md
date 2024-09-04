Title: Making Portable Digital Learning
Date: 2024-09-03 16:41
Modified: 2024-09-03 16:41
Tags: server, portable, learning, education, rpi, raspberry-pi, linux, open-source, gl.inet, python, nginx
Category: Self-Hosted
Slug: making-portable-digital-learning
Authors: joestan
Summary: With all of these 4-H activities that I've been helping with, I've been in my car. A lot. That means that I don't always have access to great internet, great resources, and I can't always connect home to my servers, there. I've decided to combat that by building a single, portable network. A network in a box, if you will. Here's how I did it.



::uml:: format="svg" alt="Portable 'Network in a Box'" title="Porta-Network" width="100%"
!theme blueprint

nwdiag {
  network open_unsecured {
      address = "210.x.x.x/24"

      user [description = "<&person*4.5>\n user1"];
      // set multiple addresses (using comma)
      web01 [address = "210.x.x.1, 210.x.x.20",  description = "<&cog*4>\nweb01"]
      web02 [address = "210.x.x.2",  description = "<&cog*4>\nweb02"];

  }
  network 4-H_Mobile {
      address = "192.168.8.x/24";

      web01 [address = "172.x.x.1"];
      web02 [address = "172.x.x.2"];
      db01 [address = "172.x.x.100",  description = "<&spreadsheet*4>\n db01"];
      db02 [address = "172.x.x.101",  description = "<&spreadsheet*4>\n db02"];
      ptr  [address = "172.x.x.110",  description = "<&print*4>\n ptr01"];
  }
}
::end-uml::

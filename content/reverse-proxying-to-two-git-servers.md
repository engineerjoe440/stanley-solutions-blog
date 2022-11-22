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

::uml:: format="svg" alt="Basics of a Reverse Web Proxy" title="Basics of a Proxy" width="35%"
   !theme hacker
    skinparam actorStyle awesome
    actor User
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

There's a number of proxy services available out there... Just to name a few:

* [NGINX](https://www.nginx.com/) (my default selection)
* [HAProxy](http://www.haproxy.org/)
* [traefik](https://traefik.io/)

There's others, too, I'm just most familiar with NGINX, and the others here, to a much lesser extent.

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
    gl80 --> GitLab
    gl443 --> glnginx
    glnginx --> GitLab

    ge80 --> ge443
    ge80 --> Gitea
    ge443 --> genginx
    genginx --> Gitea
::end-uml::

## But, Joe, You Said Something about SSH?

Yep! That's right!

If you're not terribly familiar with Git, let me just say that you can clone either over HTTP(S) or SSH. In the following images, see how both GitLab and Gitea support
HTTPS and SSH:

<img src="{attach}/images/gitea-clone.png" align="left" style="width: 55%; margin: 2%;" alt="Gitea Clone">
<img src="{attach}/images/gitlab-clone.png" align="right" style="width: 35%; margin: 2%;" alt="GitLab Clone">

<img src="{attach}/images/laughing-hysterically.gif" align="right" style="width: 20%" alt="Laughing Hysterically">

SSH is often just a bit faster, and brings other perks, but it can't be proxied in quite the same way as HTTP traffic. That's because SSH doesn't use hostnames in headers
in the way that HTTPS does. But, we can do some unique things to make some of this work to our liking.

> So, what DO we do, then?

In this case, we can customize the SSH services for both endpoints! We just need to use non-standard ports, and inform both GitLab and Gitea that they're using those
specific ports. That way when users clone repositories, the non-standard ports will be in the URL, and used automagically!

## Customizing GitLab

I want to highlight a few points, here. Notably, for my specific configuration.

#### HTTPS Relevant Configuration

I want to call out how I got the HTTPS routing for GitLab working:

```ruby
## GitLab URL
##! URL on which GitLab will be reachable.
##! For more details on configuring external_url see:
##! https://docs.gitlab.com/omnibus/settings/configuration.html#configuring-the-external-url-for-gitlab
##!
##! Note: During installation/upgrades, the value of the environment variable
##! EXTERNAL_URL will be used to populate/replace this value.
##! On AWS EC2 instances, we also attempt to fetch the public hostname/IP
##! address from AWS. For more details, see:
##! https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instancedata-data-retrieval.html
external_url "https://gitlab.stanleysolutionsnw.com"

... more ...

##! **Override only if you use a reverse proxy**
##! Docs: https://docs.gitlab.com/omnibus/settings/nginx.html#setting-the-nginx-listen-port
nginx['listen_port'] = 80

##! **Override only if your reverse proxy internally communicates over HTTP**
##! Docs: https://docs.gitlab.com/omnibus/settings/nginx.html#supporting-proxied-ssl
nginx['listen_https'] = false
```

#### SSH Relevant Config

I'll also highlight the config options I needed to get SSH working in the way I wanted:

```ruby
### GitLab Shell settings for GitLab
gitlab_rails['gitlab_shell_ssh_port'] = 8022
# gitlab_rails['gitlab_shell_git_timeout'] = 800
```

## Customizing Gitea

For Gitea, there were a few less things that I needed to tweak, but I did have to modify both the application's INI file, and the docker-compose configuration.

#### Application Config

```ini
[server]
APP_DATA_PATH    = /data/gitea
DOMAIN           = gitea.stanleysolutionsnw.com
SSH_DOMAIN       = gitea.stanleysolutionsnw.com
HTTP_PORT        = 3000
ROOT_URL         = https://gitea.stanleysolutionsnw.com/
DISABLE_SSH      = false
SSH_PORT         = 8023     # This is the really important line, right here!
SSH_LISTEN_PORT  = 22
LFS_START_SERVER = true
LFS_CONTENT_PATH = /data/git/lfs
LFS_JWT_SECRET   = FFqnGuw9L0Zaj6tPeJpqEQgp4yZHpPpvRcul5G9Nv1o
OFFLINE_MODE     = false
```

#### Compose File

```yaml
version: "3"

networks:
  gitea:
    external: false

services:
  server:
    image: gitea/gitea:latest
    container_name: gitea
    environment:
      - USER_UID=1000
      - USER_GID=1000
      - GITEA__database__DB_TYPE=postgres
      - GITEA__database__HOST=db:5432
    env_file:
      - .env
    restart: always
    networks:
      - gitea
    volumes:
      - ./gitea:/data
      - /etc/timezone:/etc/timezone:ro
      - /etc/localtime:/etc/localtime:ro
    ports:
      - "3000:3000"
      - "8023:22" # This is the really important line, right here!
    depends_on:
      - db
```

## Proxy-Server NGINX Streams

So, let's get back to the root of this whole thing, and I'll explain how I'm able to route these SSH channels, to begin with.

As I had alluded to, earlier, we can't just have listening servers for SSH like we can for HTTP, where the hostname will help determine the "upstream" service which
will receive the routed trafic. Instead, we need to perform a port-based approach -- thus the whole usage of 8022 and 8023 in the previous configuration samples. Adding
streams is relatively straight-forward, and I just added them to my NGINX configuration file; you know, the one located at `/etc/nginx/nginx.conf`.

To do this, you can simply configure a `stream` block to have the respective "upstreams" and their listening services. Relatively simple!

```conf
################################################################################
#
# Stanley Solutions SSH Proxies Including:
#   - GitLab
#   - Gitea
#
################################################################################

stream {

        upstream gitlab-ssh {
            server 192.168.254.5:22;
        }

        upstream gitea-ssh {
            server 192.168.254.12:8023;
        }

        # Gitlab
        server {
            listen 8022;
            proxy_pass gitlab-ssh;
        }

        # Gitea
        server {
            listen 8023;
            proxy_pass gitea-ssh;
        }
		
}
```

After this NGINX configuration is applied, it's just a matter of adding the port-forwardings to the router:

* `8022 -> 8022` Pointed at the Proxy Server
* `8023 -> 8023` Pointed at the Proxy Server

So, now, the whole SSH topology configuration looks a little more like this:

::uml:: format="svg" alt="Stanley Solutions SSH Proxy Configuration" title="Stanley Solutions SSH Proxies" width="100%"
   !theme hacker
    skinparam actorStyle awesome
    actor GitSSHUser
    cloud WAN

    GitSSHUser --> WAN

    node Home-Network {
        portin Router8022
        portin Router8023

        node Gitea as gitea-srv{
            portin "8023" as ge8023
            database Gitea
        }
        node GitLab as gitlab-srv{
            portin "22" as gl22
            portin "8022" as gl8022
            database GitLab
            component NGINX as glnginx
        }
        node Reverse-Proxy as proxy{
            portin "8022" as px8022
            portin "8023" as px8023
            component NGINX as proxynginx
        }
    }
    WAN --> Router8022
    WAN --> Router8023
    Router8022 --> px8022
    Router8023 --> px8023

    px8022 --> proxynginx
    px8023 --> proxynginx

    gl22 <-l- proxynginx
    proxynginx -l-> ge8023

    gl8022 --> glnginx
    glnginx --> GitLab
    gl22 --> GitLab

    ge8023 --> Gitea
::end-uml::

Now, at this point, upon inspecting the diagram, you may wonder a few things.

#### 1) Why is NGINX still involved in the GitLab route?

Well, this is due to the fact that although we're advertising Git-over-SSH service on port 8022, we're actually listening on port 22, still. That means that for *local*
access (*coughs* -- for me) I'll need to have some routing to support the appropriate port 8022.

#### 2) Why didn't you just point your port-forwarding at the GitLab and Gitea servers, instead of routing through NGINX?

Well, I'd like to say that this was purely because I wanted some opportunity to have some education, but if I'm honest, it's mostly because this possibility didn't occur to me.

> Oops. :/

But I guess that means this really was a learning opportunity, then , doesn't it? For now, I'm happy with the topology, and I don't think I'll change unless I find a "good-enoug" reason to.

## Conclusion

Now, I can successfully clone from both GitLab and Gitea over SSH. Whoop-whoop!!!!

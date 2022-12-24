Title: Adding Radon Sensors to Home Assistant
Date: 2022-12-24 10:40
Modified: 2022-12-24 10:40
Tags: homeassistant, home-assistant, hasio, airthings, ble, bluetooth, wireless, radon, air, quality
Category: Home-Improvement
Slug: adding-radon-sensors-to-homeassistant
Authors: Joe Stanley
Summary: Radon - an colorless, oderless gas. Sounds familiar, right? But you've probably heard that phrase in relation to other gasses like the carbon-monoxide, or perhaps natural gas. Radon poses health threats, as well, but with the added benefit of radiation. Scared yet? Don't worry.

[cdc]: https://www.cdc.gov/nceh/features/protect-home-radon/index.html
[airthings]: https://www.airthings.com/resources/radon-detection

## What is Radon, Anyway?

The [CDC][cdc] explains that Radon is:

> " ...the second leading cause of lung cancer after cigarette smoking. If you smoke and live in a home with high radon levels, you increase your risk of developing lung cancer. Having your home tested is the only effective way to determine whether you and your family are at risk of high radon exposure.
> 
> Radon is a radioactive gas that forms naturally when uranium, thorium, or radium, which are radioactive metals break down in rocks, soil and groundwater. People can be exposed to radon primarily from breathing radon in air that comes through cracks and gaps in buildings and homes. Because radon comes naturally from the earth, people are always exposed to it. "

Luckily for me, I don't smoke. So some of that problem is a non-starter. Buuuut... Have you
seen [my basement](https://blog.stanleysolutionsnw.com/more-servers-in-the-basement.html)?
Yeah... that's where this all comes from. And the photos in that post don't even capture the
wet season.

Hah!

## What can be done?

The [CDC][cdc] goes into some detail about some options which exist to support annual tests for
Radon, but there's also technology that can help; and, have you met me? Of course I want to use
the technology! That's the fun part.

Airthings is a pretty neat company. They offer a digital air-quality and Radon sensing solution,
and they even make their technology accessible *without* needing the cloud! For self-hosters like
me, that's pretty exciting. You can read more about
[what thoughts Airthings share regarding Radon detection methods on their website][airthings].

## The Sensor

Airthings' Wave Plus sensor is just what I needed. I picked one up last year from Amazon, but
you can see from [Airthings' store](https://shop.airthings.com/US_EN/wave-plus.html) that these
things are a bit on the spendy side. Still not bad.

<img src="https://shop.airthings.com/media/catalog/product/cache/2634002fa3d4cd41f308759bc7b7f687/a/i/airthings-wave-plus-hero-image-for-e-commerce-front.jpg" width="40%; margin: 10px;" alt="Airthings Wave Plus" align="left">

This little gadget supports Bluetooth Low Energy (BLE), and therefore, doesn't really need
internet access. In fact, Airthings seems to know their audience, since they support some Python
scripts in [their GitHub repository](https://github.com/Airthings/waveplus-reader). Their
documentation for using the scripts is nice and simple, too. Pretty straight-forward to get
up-and-running if you've got Python 2.

That's right. I said *Python 2*. Unfortunately, although there's a
[pull request](https://github.com/Airthings/waveplus-reader/pull/8) open to add Python 3 support,
it hasn't been resolved yet.

No matter!

I've taken the liberty of snagging the updated Python 3 content where that PR originates from, and
it certainly "checks out."

## Incorporating Into Home Assistant

To go over the background, quickly:

My Home Assistant is being served from a Docker container on an old Compaq computer.

<img src="{attach}/images/2022-12-24_11-46.png" width="60%; margin: 10px;" alt="My Old Compaq Computer" align="right">

It's a 32-bit monster running Debian 11. Slow as heck, but it plugs along alright. I recently
rebuilt the OS from the ground up to take advantage of a second hard-drive in the machine which,
frankly, I'd forgotten about until recently. That's meant that I can shove the whole config back
into a single repository in my GitLab server. Quite nice, if you ask me.

I digress.

The server is WAY too old to support Bluetooth in its existing hardware. But that's what USB is for, right? So I hooked up a little USB dongle which provides BLE support. Now, I just needed to pass it all through to Home Assistant.

I'll go through the steps I took, next, but I want to tell you; this isn't *exactly* the order
that I used initially. Would you expect me to have been that smart? To have put it together
correctly on the first pass?

***As if!***

### Installing the System Requirements

So, really, the only package that I *needed* was `bluez`, but for some of the Airthings scripts,
there were a few others, so I'll list them all here...

```bash
sudo apt-get install bluez libglib2.0-dev -y
```

To get the Airthings scripts running, I also needed a few Python packages. They were installed
with:

```bash
sudo python3 -m pip install bluepy tableprint
```

Again... not entirely necessary, but could be useful if you're like me, and like debugging.

### Preparing the System

With `bluez` installed, I could now turn on the Bluetooth system. I'm not entirely sure whether
this is necessary for Home Assistant's purposes, but it's useful from the Airthings script
point-of-view.

##### Turn on Bluetooth!

```bash
joestan@hasio:~$ sudo bluetoothctl
[bluetooth]# power on
[bluetooth]# quit
joestan@hasio:~$
```

##### Set Bluetooth Dongle to Specific Device Alias

Again, not totally sure if this was necesssary, but even if it wasn't, I like the outcome of
having a specifically named USB device show up. Makes things nice!

Listing my USB devices with `lsusb`, I was able to determine the appropriate device:

```bash
joestan@hasio:~$ lsusb
Bus 001 Device 002: ID 1a40:0101 Terminus Technology Inc. Hub
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 003 Device 002: ID 0a5c:21e8 Broadcom Corp. BCM20702A0 Bluetooth 4.0
Bus 003 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
Bus 002 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
```

I needed to edit my udev-rules and add a custom alias.

```bash
sudo nano /etc/udev/rules.d/99-my_rules.rules
```

And then, since it's pretty clear that Bus 3 Device 2 is the one I'm looking for, I could update
my udev file accordingly:

```conf
ACTION=="add", ATTRS{idVendor}=="0a5c", ATTRS{idProduct}=="21e8", SYMLINK+="btooth"
```

Now, after a restart, I've got that device listed properly when I `ls /dev`:

```bash
joestan@hasio:~$ ls /dev
agpgart          mqueue    stderr  tty29  tty52    vcs3
autofs           net       stdin   tty3   tty53    vcs4
block            null      stdout  tty30  tty54    vcs5
bsg              nvram     tty     tty31  tty55    vcs6
btooth           parport0  tty0    tty32  tty56    vcsa        #<--- Look!
btrfs-control    port      tty1    tty33  tty57    vcsa1
bus              ppp       tty10   tty34  tty58    vcsa2
char             psaux     tty11   tty35  tty59    vcsa3
console          ptmx      tty12   tty36  tty6     vcsa4
core             pts       tty13   tty37  tty60    vcsa5
cpu_dma_latency  random    tty14   tty38  tty61    vcsa6
cuse             rfkill    tty15   tty39  tty62    vcsu
disk             rtc       tty16   tty4   tty63    vcsu1
fd               rtc0      tty17   tty40  tty7     vcsu2
full             sda       tty18   tty41  tty8     vcsu3
fuse             sda1      tty19   tty42  tty9     vcsu4
hpet             sda2      tty2    tty43  ttyS0    vcsu5
hugepages        sdb       tty20   tty44  ttyS1    vcsu6
hwrng            sdb1      tty21   tty45  ttyS2    vfio
initctl          sdb2      tty22   tty46  ttyS3    vga_arbiter
input            sdb3      tty23   tty47  uhid     vhci
kmsg             sg0       tty24   tty48  uinput   vhost-net
log              sg1       tty25   tty49  urandom  vhost-vsock
loop-control     shm       tty26   tty5   vcs      watchdog
mapper           snapshot  tty27   tty50  vcs1     watchdog0
mem              snd       tty28   tty51  vcs2     zero
```

##### Update Docker Container Command

I'm lazy.

Although I haven't converted this machine to use `docker-compose`, I use a shell script to do
the heavy lifting for me, and get the latest container, update and redeploy it. So, when it came
time to update the command and make sure that I pass the Bluetooth device and `dbus` into the
container, it was pretty simple, just needed to add the arguments to the command...

```sh
# Start HassIO
echo Starting Hasio
sudo docker run -d --name homeassistant --restart=unless-stopped \
  -v /home/joestan/stanleyassistant/homeassistant:/config -v /etc/localtime:/etc/localtime:ro \
  -v /run/dbus:/run/dbus:ro --privileged --network=host --device /dev/btooth \
  ghcr.io/home-assistant/home-assistant:stable
```

Notice on the second line from the bottom, I'm using the following commands:

* `-v /run/dbus:/run/dbus:ro`: This maps the `dbus` volume into the container appropriately.
* `--device /dev/btooth`: For good measure, this maps the Bluetooth device into the container.

Those were really the only additions that were needed. Then it was just a matter of restarting
the container with the new arguments, and adding the config of the device in the HA Web-UI.

## Closing Thoughts

Well, I think I learned a few things with this experience. Nothing terrible, or drastic. Just
some good points and things to remember. Kind of a nice accomplishment on a Christmas Eve, if you
ask me!

I love the tight integrations that can be offered with Home Assistant, and I'm really pleased with
my Airthings Wave Plus sensor. I love the fact that I can use it in my local system and start
monitoring for "bad gas."

Let me know if you have any thoughts or other experiences!
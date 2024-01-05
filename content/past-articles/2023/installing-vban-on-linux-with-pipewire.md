Title: Installing VBAN on Linux Systems with Pipewire
Date: 2022-12-18 10:00
Modified: 2022-12-18 10:00
Tags: vban, audio, networking, linux, pipewire, alsa, sound
Category: Audio
Slug: installing-vban-on-linux-with-pipewire
Authors: Joe Stanley
Summary: I recently decided to drop Windows (finally), and move to Linux, full-time. But that means moving to Pipewire; which is both exciting and slightly daugnting. You see, to make the move, I need to get VBAN working on Linux, and talking to Pipewire. Hmm. Time to do some digging...

[installing-vban]: https://blog.stanleysolutionsnw.com/networked-audio-using-vban-and-rpi.html
[keeping-vban-running]: https://blog.stanleysolutionsnw.com/spam-the-vban-for-non-stop-audio.html
[vban-python]: https://blog.stanleysolutionsnw.com/a-better-way-to-integrate-with-voicemeeter.html
[docs]: https://github.com/quiniouben/vban

### Reason for being here.

That's right, I'm finally moving away from Windows as my daily driver at home. Making the move
to Kubuntu. I'm much happier with the change, but I do need to fix a reasonable set of things
and get VBAN working to make sure that my audio is still uninterrupted!

What's `VBAN`, you ask? Well, go check out my other articles:
* [networked-audio-using-vban-and-rpi][installing-vban]
* [spam-the-vban-for-non-stop-audio][keeping-vban-running]
* [a-better-way-to-integrate-with-voicemeeter][vban-python]

In a nutshell, however, I use VBAN as a low-latency audio networking solution for my home.
It's really helped to bring whole-home audio together quite nicely. Analog can still be "easier"
in some regards, but it's more time and effor to run those wires, sometimes.

### Installing VBAN

This hasn't really changed all that much since my article about
[installing VBAN on the Raspberry Pi][installing-vban]. It starts with installing the basics.

```shell
sudo apt install libasound-dev autoconf automake
```

Cloning the repository...

```shell
git clone https://github.com/quiniouben/vban.git
```

Running the autogen script...

```shell
./autogen.sh
```

Setting up for only alsa...

```shell
./configure --enable-alsa --disable-pulseaudio --disable-jack
```

Then install with `make` like the [docs][docs] show.

---

Wanna just run one script? Yeah, me too...

```bash
#!/usr/bin/bash
sudo apt-get install libasound2-dev autoconf automake -y

cd /home/$(whoami)/Downloads

git clone https://github.com/quiniouben/vban.git

cd vban

./autogen.sh

./configure --enable-alsa --disable-pulseaudio --disable-jack

make

# I needed sudo, you might not? Too lazy to bother checking...
sudo make install
```

## Getting Alsa Working?

Well... that's the next step. I seem to be having "fun" with that, again. I'll have to
dig around some more. I'm leaving this post incomplete, because I want to report back when I get
the darned thing working.

> ... more soon ...

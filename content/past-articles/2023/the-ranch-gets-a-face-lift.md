Title: The Ranch (KRNC) Gets a Face Lift
Date: 2023-01-08 12:00
Modified: 2023-01-08 12:00
Tags: linux, audio, python, ffmpeg, sound, terminal, command-line, flet, flutter, application, krnc
Category: Python
Slug: the-ranch-gets-a-face-lift
Authors: Joe Stanley
Summary: So, I've got an old (1992) Ford pickup, and it's got a newer-ish stereo. I love keeping my favorite tunes on a USB stick that I can play everything from, but I HATE it when the volume changes from one song to the next. I go from barely being able to hear the music to having my eardrums blown out in 0.5 seconds. So, I've come to the conclusion that I need to fix that. With PYTHON!

Like I'd mentioned; I absolutely *HATE* it when the audio in my car goes from practically inaudible to raising the dead.

> Not fun.

So the question becomes, how do I do something about this problem of mine? What can I do to equalize the volume levels?
Well, of course I can use an application to compress and normalize the volume of tracks. It's something I was quite
accustomed to from my old radio days. You see, that's pretty common to do for a radio-station's imaging/branding tracks.
You know... the little quips you hear between songs like "Your favorite station for the 90's through now!" etc. Most of
those type of track go through some kind of compressor prior to be loaded into the on-air playback system, and what's
more, most stations use a real-time compressor that takes the fully-mixed audio stream from the on-air studio and
compresses that for going out on the air. That's twice the compression for those of you who are counting, but normally
the compression used for the imaging tracks is specifically customized such that it will "play nicely" with the in-line
compressor in the studio.

Ok, so that was a diversion from the root of this conversation, but I hope it gives you some of the background to
understand the next bit of this topic.

-----

Compression is a slick way of bringing the low-volume stuff up to make sure it's audible, and bringing the loud stuff
down a bit, without making the whole thing sound terrible. I found a GIF that does its best to show some of this. It's
not great, but I couldn't be bothered to make my own. Hah!

<img src="https://audiophilestyle.com/uploads/monthly_2019_08/510421229_GrundmanvsDownloadWavforms.gif.2fb2cdf545abce8f61fdc881d4ac9db0.gif" width="100%" alt="compressing audio">

There's a number of compressors available, and they're all a bit touchy, but there's some really cool ways to do it with
Linux command-line utilities. Namely [`ffmpeg`](https://ffmpeg.org/) -- the universal, quintessential audio utility.

If there's an app on Linux or Windows that works with audio, it almost certainly has some compatibility or reliance on
ffmpeg.

With ffmpeg, I can do lots of things with audio... basically whatever I wanted to... but to name a few things:

* compress
* normalize
* filter
* equalize
* and much, *much* more...

So, I did some digital spelunking and found a handful of little sets of arguments I liked for some general filters:

| What I call it | What the command is                                                                                 |
|----------------|-----------------------------------------------------------------------------------------------------|
| "default"      | `-filter_complex compand=attacks=0:points=-80/-900\|-45/-15\|-27/-9\|0/-7\|20/-7:gain=5`            |
| "normalize"    | `-filter:a "dynaudnorm"`                                                                            |
| "light"        | `-filter:a compand=.3\|.3:1\|1:-90/-60\|-60/-40\|-40/-30\|-20/-20:6:0:-90:0.2`                      |
| "heavy"        | `-filter:a compand=0\|0:1\|1:-90/-900\|-70/-70\|-30/-9\|0/-3:6:0:0:0`                               |

So clearly, I've got a good little set of compressors and filters. Still, would you remember any of those commands? I
certainly won't. So I'd like to have a little tool do that for me.

At the same time, I've also been wanting to try out the new Python tool [`Flet`](https://flet.dev/) for building Flutter
based applications. No, I don't want to write Dart applications, but I wouldn't mind if there's a layer between me and
that mess.

So... I got to work and rebuilt my
["Universal Song Barn Manager" Application](https://gitlab.stanleysolutionsnw.com/krnc/usb-manager). Do you notice the
play-on-words in the name? *USB* Manager...

<img src="https://gitlab.stanleysolutionsnw.com/krnc/usb-manager/-/raw/master/images/SongBarn.png" width="100%" alt="KRNC - Universal Song Barn Manager">

I want to toot my own horn here a little bit. I built this app in *one, single day*.

Admittedly, I went back and have touched up things in subsequent days, but the original application was written in one
day. I'm kinda proud of that.

So, the application has a relatively simple workflow:

1. Open app
2. Add songs to your "barn" (record file) with the app's "`+`" button
3. Change the filtering selection as desired, change the track's "Title" if needed
4. Select the USB drive you want to store the files on
5. Load the drive
6. Listen and enjoy!

-----

Now... I've got some work left to do. I still want to get the app set up so that it can use a "Saddle Bag" system to
support retrieving short audio clips as "radio imaging" because I'm just that kind of nerd. That'll have to come soon.

Take a look at the GitLab information if you'd like. Let me know what you think, and feel free to use it for your own
needs if you'd like!
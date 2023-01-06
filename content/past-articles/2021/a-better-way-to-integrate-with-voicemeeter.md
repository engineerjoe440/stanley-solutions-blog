Title: A Better Way to Integrate with VoiceMeeter?
Date: 2021-09-12 17:07
Modified: 2021-09-15 17:38
Tags: Audio, Voicemeeter, Api, Sdk, Mixer, Python
Category: Python
Slug: a-better-way-to-integrate-with-voicemeeter
Authors: Joe Stanley
Summary: Wait... What? There's an API for VoiceMeeter? And there's already a Python API for it? Sign me up!


So, I finally sucked it up and bought an Intel NUC to run as my own mini audio-server. For what purpose,
you ask? Well, so that I can have an "always on" [VBAN](https://vb-audio.com/Voicemeeter/vban.htm) server
where I can route audio through-out my house. From my desktop, my laptop, my mixer, my stereo.... All
over!

Now, I did run into a little trouble in the process. My little NUC is mounted nicely out of the way at my
desk in my study. It looks great, and runs great... buuuuut... There's one little problem.

When I connect or disconnect over a Remote Desktop (RDP) connection it gets, shall we say, a little mixed
up. In fact, the VoiceMeeter audio engine falls all over itself and gets tangled up. Now, to get around
this problem, I can restart the audio engine, or the software itself. So I started looking into how to
automate the kick-in-the-pants the software needed. Mind you, I'd done this before by using Python to find
the process ID that VoiceMeeter was associated with, and kill it, restarting a moment later. But that's
boring and slow. So I did some Googling...

Turns out, VoiceMeeter has an [API](https://forum.vb-audio.com/viewtopic.php?f=8&t=346)! FANTASTIC!

Now, I realize that that's a C-API, and I'd much rather do my programming in Python. I don't really want
to fuss with installing GCC on my little NUC. SO... I started investigating how to wrap the C-API with
Python. It's something I'd never done before, but I figured it must be possible! Once more, I turned to
the internet wizards, and found a very [nice little article on StackOverflow](https://stackoverflow.com/a/252473/10406011)
on how to wrap a C-level DLL with Python.

I used that article and proved to myself that, YES, I can write Python code to hit the DLL. But, it
occurred to me, that maybe somebody else had already done that work.

Back to Google...

EUREKA! Turns out that someone ([Christian Volkmann](https://github.com/chvolkmann), to be specific) had
already written a full API against the DLL. It's all in Python, and it's glorious! Here...
[Go take a look!](https://github.com/chvolkmann/voicemeeter-remote-python)

So all that left for me was whacking out a little script to run in the background, monitor for new RDP
connections, and restart the audio engine when the connection state changed. Here's what that looked
like:

```python
# vmeetermanager - an automated tool to keep VoiceMeeter running correctly.
# (c) 2021 - Stanley Solutions | Joe Stanley

# Imports
import voicemeeter
import subprocess
import time


# Define function to determine rdp connection
def is_rdp_connected():
    args = ["netstat", '-n', '|', "find", '":3389 "']
    resp = subprocess.run(' '.join(args), shell=True, capture_output=True)
    if "ESTABLISHED" in resp.stdout.decode('utf-8'):
        return True
    return False # Default


# Main Body
if __name__ == "__main__":
    last_state = False
    # Establish VoiceMeeter Connection
    while True:
        try:
            with voicemeeter.remote("banana") as vmr:
                # Run Loop
                while True:
                    # Determine Connection State
                    connected = is_rdp_connected()
                    changed_state = connected != last_state
                    last_state = connected
                    # If the state has changed, restart audio engine
                    if changed_state:
                        print(f"RDP Connection State Changed to: CONNECTED={connected}")
                        time.sleep(0.25)
                        vmr.restart()
                    # Don't overburden the systems
                    time.sleep(1)
        except Exception:
            print("VoiceMeeter Hasn't Started Yet...")
            time.sleep(3)
```

### What Else Will Come?

Goodness, there's so many other things that I can do with this now. Imagine having a full web-based front
end that I could use to control it! That would be pretty awesome, wouldn't it? I'll really have to do
some more exploring with this!

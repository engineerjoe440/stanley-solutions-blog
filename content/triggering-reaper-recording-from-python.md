Title: Triggering REAPER Recording from Python
Date: 2026-04-15 21:44
Modified: 2026-04-15 21:44
Tags: audio, daw, python, reaper, scripting, stream-deck, ubuntu, linux
Category: Python
Slug: triggering-reaper-recording-from-python
Authors: Joe Stanley
Summary: Python, REAPER, and a Stream Deck? What do those things have in common? Is this one of those weird games? Not really. This is how I hooked up a Stream-Deck controller to control my REAPER audio software.

Did you think you needed new ways of controlling your [REAPER audio software](https://www.reaper.fm/). I knew it! I knew it. Well, today is your lucky day.

I did this a while back, and it was great... until I updated my Ubuntu installation, and started using a newer version of Python. Best I can tell, REAPER doesn't
actually support Python 3.11 or newer. *Somebody want to prove me wrong? Leave a comment! I'd love to hear a better way to do this.* This left me flailing; looking
for a better solution so I could still have a big "Record" button on my Stream-Deck.

This is all because REAPER has this cool system that allows you to interact with the software through a scripting interface, and even drive some actions directly
through Python. Very cool for geeks like me!

Now... this would've taken me quite a while, so I had a friend help me with some of the research. As this whole thing breaks down, you ultimately need to do the
following:

1. Install `pyenv`
2. Install **Python 3.10** with shared-library support
3. Configure REAPER to use that Python version
4. Install `reapy-next`
5. Create a working **toggle recording** script

---

## 1. Install `pyenv`

### Install dependencies

Here's a list of packages that will likely be needed to help get your `pyenv` system up and running.

```bash
sudo apt update
sudo apt install -y build-essential libssl-dev zlib1g-dev 
  libbz2-dev libreadline-dev libsqlite3-dev curl 
  libncursesw5-dev xz-utils tk-dev libxml2-dev 
  libxmlsec1-dev libffi-dev liblzma-dev
```

### Install `pyenv`

```bash
curl https://pyenv.run | bash
```

### Add `pyenv` to your shell

Add these lines to `~/.bashrc`:

```bash
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

Reload your shell:

```bash
source ~/.bashrc
```

---

## 2. Install Python 3.10 with shared-library support

REAPER **requires** the Python shared library (`libpython3.10.so`).

Install Python 3.10:

```bash
env PYTHON_CONFIGURE_OPTS="--enable-shared" pyenv install 3.10.13
```

Set it as your working version:

```bash
pyenv shell 3.10.13
```

Verify the `.so` exists:

```bash
find ~/.pyenv/versions/3.10.13 -name "libpython3.10*.so"
```

Expected output:

```text
~/.pyenv/versions/3.10.13/lib/libpython3.10.so
```

---

## 3. Install `reapy-next`

`reapy-next` is the Python package that provides a whole slew of functionality
for interacting with REAPER through a Python lens. And hey, let's be honest... I'm basically blind to anything *other*
than Python.

```bash
pip install reapy-next
```

---

## 4. Configure REAPER to use `pyenv` Python 3.10

REAPER must be pointed at:

- The Python **interpreter**
- The Python **shared library (.so)**

Open:

> **Options → Preferences → Plug-ins → ReaScript**

Set:

**Python interpreter:**

```text
/home/joestan/.pyenv/versions/3.10.13/lib
```

**Python library (.so):**

```text
libpython3.10.so
```

Restart REAPER.

---

## 5. Ensure REAPER actually uses Python 3.10

With REAPER open, run the following terminal command:

```bash
~/.pyenv/versions/3.10.13/bin/python3 -c "import reapy; reapy.configure_reaper()"
```

That command should immediately return without any error. If it hangs, and a message appears in REAPER regarding some
Python 3.12 path that cannot be found, it's time to get to `grep`in'.

### 5.1 Fix REAPER config files

If you saw Python 3.12 above, it's time to fix your `reaper.ini`. I had to do some searching to actually find that.

Run the following command to find any locations that are still referencing Python 3.12

```bash
grep -Rni "python3.12" ~/.config/REAPER
```

Then go pop those files open and change those full Python paths to the `pyenv` equivalents shown above.

Restart REAPER again.

---

## 6. Install the `ReaCmd` Package

That's right. You guessed it.

> I wrote another Python package.

But this one's small! You can snag it from [GitHub](https://github.com/engineerjoe440/ReaCmd). To make it easy, just
install that package in your `pyenv` environment:

```bash
~/.pyenv/versions/3.10.13/bin/python3 -m pip install git+https://github.com/engineerjoe440/ReaCmd.git
```

Now you should have a script accessible to actually operate the record-toggle operation.

```bash
~/.pyenv/versions/3.10.13/bin/rea-record
```

*Voila*

---

# Done.

You now have:

- A working pyenv Python 3.10 installation
- REAPER correctly embedding Python 3.10
- A working `reapy-next` client script that toggles recording

I hope you find this helpful. I'm sure I'll be coming back to that to fix my system again in the future!

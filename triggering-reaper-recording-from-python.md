Title: Triggering REAPER Recording from Python
Date: 2026-04-15 21:44
Modified: 2026-04-15 21:44
Tags: audio, daw, python, reaper, scripting
Category: Python
Slug: triggering-reaper-recording-from-python
Authors: Joe Stanley
Summary: todo


# REAPER + pyenv + Python 3.10 + reapy-next Setup Guide

This guide explains how to:

- Install **pyenv**
- Install **Python 3.10** with shared-library support
- Configure REAPER to use that Python version
- Install `reapy` (server) and `reapy-next` (client)
- Create a working **toggle recording** script

---

## 1. Install pyenv

### Install dependencies

```bash
sudo apt update
sudo apt install -y build-essential libssl-dev zlib1g-dev 
  libbz2-dev libreadline-dev libsqlite3-dev curl 
  libncursesw5-dev xz-utils tk-dev libxml2-dev 
  libxmlsec1-dev libffi-dev liblzma-dev
```

### Install pyenv

```bash
curl https://pyenv.run | bash
```

### Add pyenv to your shell

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

```
~/.pyenv/versions/3.10.13/lib/libpython3.10.so
```

---

## 3. Install `reapy` (server) and `reapy-next` (client)

### Install reapy (inside Python 3.10)

```bash
pyenv shell 3.10.13
pip install reapy
```

### Install reapy-next (your external client)

```bash
pip install reapy-next
```

---

## 4. Configure REAPER to use pyenv Python 3.10

REAPER must be pointed at:

- The Python **interpreter**
- The Python **shared library (.so)**

Open:

**Options → Preferences → Plug-ins → ReaScript**

Set:

**Python interpreter:**

```
/home/joestan/.pyenv/versions/3.10.13/bin/python3.10
```

**Python library (.so):**

```
/home/joestan/.pyenv/versions/3.10.13/lib/libpython3.10.so
```

Restart REAPER.

---

## 5. Ensure REAPER actually uses Python 3.10

Inside REAPER, run this ReaScript:

```python
from reaper_python import *
import sys
RPR_ShowConsoleMsg(sys.executable + "n")
```

Expected output:

```
/home/joestan/.pyenv/versions/3.10.13/bin/python3.10
```

If you see Python 3.12, fix your `reaper.ini`:

```bash
nano ~/.config/REAPER/reaper.ini
```

Update these lines:

```
reascript_python3_path=/home/joestan/.pyenv/versions/3.10.13/bin/python3.10
reascript_python3_dll=/home/joestan/.pyenv/versions/3.10.13/lib/libpython3.10.so
```

Restart REAPER again.

---

## 6. Start the reapy server inside REAPER

In REAPER:

**Actions → Show Action List → Run**

Search for:

```
activate_reapy_server.py
```

Run it once, or set it to auto-start.

This enables external scripts to connect.

---

## 7. Create a `reapy-next` toggle-recording script

Save this as `reaper-record-toggle`:

```python
#!/home/joestan/.pyenv/versions/3.10.13/bin/python3
from reapy_next import Reaper

rpr = Reaper()

state = rpr.get_play_state()  # 0=stopped, 1=playing, 2=paused, 5=recording

if state == 5:
    print("Stopping recording...")
    rpr.stop()
else:
    print("Starting recording...")
    rpr.record()
```

Make it executable:

```bash
chmod +x reaper-record-toggle
```

Run it:

```bash
./reaper-record-toggle
```

---

# Done.

You now have:

- A working pyenv Python 3.10 installation  
- REAPER correctly embedding Python 3.10  
- The reapy server running inside REAPER  
- A working `reapy-next` client script that toggles recording  

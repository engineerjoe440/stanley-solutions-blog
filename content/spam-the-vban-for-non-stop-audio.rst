Spam the VBAN for Non-Stop Audio
################################

:date: 2021-02-15 20:22
:modified: 2021-02-15 20:43
:tags: VBAN, Audio Network, Raspberry Pi, Python, Linux
:category: Raspberry Pi
:slug: spam-the-vban-for-non-stop-audio
:authors: Joe Stanley
:summary: When things get sticky, leave it to Python to keep the wheels greased!


.. _recent article: https://blog.stanleysolutionsnw.com/networked-audio-using-vban-and-rpi.html

In a `recent article`_ I wrote about how I'd started to integrate more of my house's
audio system with a networked audio protocol known as "VBAN". I'd gotten some great
use out of the system, but I'd started running into some problems more recently...

You see, for some reason, if I were streaming some audio to my Raspberry Pi, and the
stream dropped into a lull (i.e. between songs, say) I'd often see some pretty nasty
buffer errors from Alsa. Now, I could've dug into it much deeper and tried to get to
the root of the problem in `C`, but I didn't really feel like it. Instead, I thought
I'd just throw some Python at it! So after spending an intermittent afternoon
reminding myself how the `subprocess` module works, and debugging my own madness, I
got a working script that I use as a *systemd* service.

.. code-block:: Python
   
   # VBAN Receiver in Python
   
   # Imports
   import subprocess
   
   # Executor Function
   def execute(cmd):
       popen = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT, universal_newlines=True)
       while True:
           for stdout_line in iter(popen.stdout.readline, ""):
               yield stdout_line, popen
       popen.stdout.close()
       return_code = popen.wait()
       if return_code:
           raise subprocess.CalledProcessError(return_code, cmd)
   
   # Define Attributes
   MASTER_PC_IP = "<your-ip-here>"
   LOG_FILE = '/var/vban_log.log'
   
   # Define Command and Args
   EXECUTABLE = "/usr/local/bin/vban_receptor"
   ARGS = ["-i", MASTER_PC_IP, "-p", "6980", "-s", "StereoPi", "-d", "front", "-q", "0"]
   
   CALL = [EXECUTABLE]
   CALL.extend(ARGS)
   
   # Call the System
   while True:
       with open(LOG_FILE, 'a') as logFile:
           for output, proc_handle in execute(CALL):
               print(output, end='')
               logFile.write(output)
               # Catch Error
               if "Error: alsa_write:" in output:
                   print("Failure... Python intervening!")
                   proc_handle.kill()
                   proc_handle.wait()
                   break # Continue While Loop - Call Again
   # END


With that magic little Python script, I basically kick VBAN in the butt every time
that Alsa decides to be unfriendly (which happens quite regularly) by killing the
process, and then starting it right back up. With the magic of computers, this
happens very fast, and as I'd briefly mentioned earlier, it only seems to really
play into the "mix" in-between songs anyway. So after building the script, giving
it a nice little test drive, and scrutinizing my Raspberry Pi; I thought it was
time to build it back into my simple little service.

.. code-block:: ini
   
   # /etc/systemd/system/vbanstereorx.service
   # vbanstereorx.service
   # VBAN Receptor Stereo Service
   
   [Unit]
   Description= VBAN Stereo Receptor
   
   [Service]
   Type=simple
   ExecStart=/usr/bin/python3 /home/vbanner.py
   Restart=always
   
   [Install]
   WantedBy=multi-user.target


I'm sure I'll be back to crack the hood back open on this one at some point, but
for now, I'm happy to stream my music back to my cabinet stereo with the power of
Linux.



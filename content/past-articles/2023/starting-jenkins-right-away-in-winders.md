Title: Starting Jenkins Right Away in Winders
Date: 2022-10-24 16:25
Modified: 2022-10-24 16:25
Tags: devops, jenkins, ci/cd, continuous-integration, continuous-deployment, build-systems, automation, windows
Category: DevOps
Slug: starting-jenkins-right-away-in-winders
Authors: Joe Stanley
Summary: Jenkins is a powerful, albeit confusing, tool. You can structure all manner of automated processes to build source code, distribute packages, and automate the boring stuff. It's great! But Jenkins and Windows (or... *Winders*) don't always play nicely. I learned this the hard way in my "day-job" and had to find a technique to resolve some of this bad-behavior. So hopefully you might find this helpful!


> Let me begin by describing the circumstances.

As it turns out, in some applications, Jenkins must be run in a full UI-based environment to function properly with some tools. Notably, some of the tools I use in my day-to-day
work. A colleague and I were working on getting Jenkins running in build nodes to support automated package builds at work. Challenge is, we needed the full UI, and that's not
a "standard" configuration for Jenkins nodes on Windows. So we had to do some exploring. 

Most commonly, Jenkins agents will run as part of a "scheduled task" on a Windows host. However, this has some inherent limitations that we ran into. Specifically, some very
peculiar (and specific) C# challenges. As it turns out, those issues were only really present if the Jenkins agent was running as a desktop-environment-less task. That said,
there's not a clean way (that I found, at least) to make a task run in a full desktop environment. This left us scratching our heads to find a way to make Jenkins run
automagically in a desktop.

> Hmmm...

Eventually, I stumbled upon a potential solution! We could define a "startup user" whose account is opened by default when the Windows system starts. Almost like some kind of
"kiosk mode" for windows, but specifically for our application. Now, this still took some exploration, and learning, but I finally found a way to make a default user
"automatically log in" when the system starts, and then make a simple startup script to run the Jenkins command.


##### References
* [getting Jenkins to interact with Windows desktop][getting Jenkins to interact with Windows desktop]
* [article on ServerFault][article on ServerFault]


## Instructions

#### 1) Create a batch file to start Jenkins agent
The Jenkins agent has to be run on the VM from the specified workspace directory (`C:\_jenkins` in this case), and with the appropriate token information.
So create a batch file that you can store in the Windows startup folder for the specific user. Don't worry about it's location, now, we'll come back to that later.

Create the file `jenkins_start.bat` with the following information (substituting information where needed from Jenkins' direction).

```bat
cd C:\_jenkins

java -jar agent.jar -jnlpUrl https://< HOST >/computer/< AGENT-NAME >/jenkins-agent.jnlp -secret < SECRET > -workDir "c:\_jenkins"
```

#### 2) Move the startup script to the service-user's startup folder
To make the script run as the user would, we'll need to place it in the user's startup folder.

1. As the service user, press Ctrl+r to open the "Run" launcher prompt. (or search for "Run" in the Windows start menu)
2. Enter `shell:startup` in the prompt and press Enter/click "Run"
3. Copy/Move the batch script you created previously into the startup folder which now appears on-screen

If the above steps fail, you can manually browse to the start folder as follows:

`C:\Users\< SERVICE-USERNAME >\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`

#### OPTIONALLY:
It may be valuable to restart the machine and log in as the service-user to confirm that the startup script is working as expected and connects back to the Jenkins master
with a visible console window.

#### 3) Modify the registry to make the service-user logon automatically after startup
As described in the [article on ServerFault][article on ServerFault], generate a file called `AutoLogon.reg` somewhere on the virtual machine with the following content

```ini
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon]
"DefaultDomainName"="SERVICE_ACCOUNT_DOMAIN"
"DefaultUserName"="SERVICE_ACCOUNT_USER"
"DefaultPassword"="SERVICE_ACCOUNT_PASSWORD"
"ForceAutoLogon"="1"
"AutoAdminLogon"="1"
"LegalNoticeCaption"=""
"LegalNoticeText"=""

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\AutoLogonChecked]
@="1"

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\policies\system]
"LegalNoticeCaption"=""
"LegalNoticeText"=""
```

After saving the file, right-click on it in a file explorer and select "Merge," you'll be prompted to confirm the operation; do so.

#### Restart the machine and confirm that it automatically connects to Jenkins
Restarting the machine should make use of the new registry edits and auto-login the service account user. In-so-doing will launch the startup batch-file script which will
connect to the Jenkins master through the console in a graphical session.



[article on ServerFault]: https://serverfault.com/questions/269832/windows-server-2008-automatic-user-logon-on-power-on/606130#606130
[getting Jenkins to interact with Windows desktop]: https://stackoverflow.com/questions/18906753/jenkins-windows-slave-service-does-not-interact-with-desktop

---

## Additional Improvement Notes

I think one thing I should call out is that this mechanism doesn't "restart" if a failure occurs. That is, if Jenkins crashes, it doesn't restart. But I think it could
easily be added by using some kind of `FOR`/`WHILE` loop in the batch-file to script some kind of automatic retry. Nothing crazy, just worth noting!

##### Closing Thoughts

I know there's bound to be other ways of doing this. Let me know what you've done! Tell me about your Jenkins "woes;" I'd love to hear them! Hopefully my solution will
give you some inspiration.
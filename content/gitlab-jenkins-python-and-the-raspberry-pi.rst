GitLab, Jenkins, Python, and the Raspberry Pi!
##############################################

:date: 2020-12-21 19:07
:modified: 2020-12-21 19:07
:tags: Python, Jenkins, Gitlab, Raspberry Pi, Dev Ops, GIT, CI/CD
:category: Python
:slug: gitlab-jenkins-and-the-rpi
:authors: Joe Stanley
:summary: I'm finally getting around to setting up some CI/CD systems for my self-hosted GitLab server... About Time!


    CI/CD, Dev Ops, Pipelines, Workflows, Automated Deployment

Think that's enough buzz words to catch the Google SEO engine's eye?

Probably not, I know, but I'm not going to spend anymore time on it at the moment. See,
I've got bigger items to tackle! Namely, getting Jenkins set up on a Raspberry Pi, as
the name of this article so implies.

Good news for you; I've cut out the "dirty-work" through the magic of "blog-posting."

As part of the work I've been tackling for some of the other open source projects I'm
developing, I need to develop a local (on-premises) continuous integration solution to
effectively slam my code with testing and verification. After all, what's great code
without equally great tests? I need to have the system on-premises for a couple reasons;
the largest of which being the fact that I need access to custom hardware.

    So, why a Pi? A Pi 3-B no less?!

Well, that's quite simple; actually. It's the only spare computer I have at the moment.

So now that I've thoroughly introduced you, to my reasoning, and the topic at hand;
let's get into it!

Installing Jenkins on the Pi
----------------------------

I already have GitLab set up on an old x86 laptop running Ubuntu Server 20.04, so
for this article, I'm going to focus on setting up Jenkins on a Raspberry Pi, and
getting the basics of the workflow between Jenkins and GitLab running.

#. Start with a fresh Pi (latest build of the RaspberryPiOS). I had a Pi sitting
   around with an older build of Raspbian, but that's several years old, and I
   really just wanted to start fresh.

#. Update the Raspberry Pi. Well, in the spirit of starting fresh, might as well
   update the system!

#. Install Java with:
   
   .. code-block:: console
      
      $> sudo apt-get install openjdk-11-jre


#. Verify Java Version with:
   
   .. code-block:: console
      
      $> java --version
      openjdk 11.0.9.1 2020-11-04
      OpenJDK Runtime Environment (build 11.0.9.1+1-post-Raspbian-1deb10u2)
      OpenJDK Server VM (build 11.0.9.1+1-post-Raspbian-1deb10u2, mixed mode)


#. At this point, I took some time to get the Python system up to a state that
   would be a bit more useful for me. So I installed `pip3`, and a number of
   Python packages. I suppose this could really be done at any point during this
   whole process, but I felt like this was the most sensible time.

#. Download and add the Jenkins Key with:
   
   .. code-block:: console
      
      $> wget -q -O - https://pkg.jenkins.io/debian/jenkins.io.key | sudo apt-key add -


#. Open a new file:

   .. code-block:: console
   
      $> sudo nano /etc/apt/sources.list.d/jenkins.list
   
   Then add the following line and save the file to add the Jenkins repository as
   a source:

   .. code-block:: nano
   
      deb https://pkg.jenkins.io/debian binary/


#. Next, another good `sudo apt-get update` is in order, followed by
   `sudo apt-get install jenkins`

#. Using the command listed below, you can grab the initial admin password to get
   started:

   .. code-block:: console
   
      $> sudo cat /var/lib/jenkins/secrets/initialAdminPassword


#. Now it's time to navigate to `<raspberry-pi-ip-address:8080` and use that fancy
   password to log in for the first time and start the setup wizard; or should I say
   butler?


After the "butler" has completed, it's time to get started with setting up some CI
jobs.


Preparing a Simple `pytest` Job with Jenkins
--------------------------------------------

Now, I'll caution that I this portion doesn't cover any of the GitLab/Jenkins
interfacing, maybe I'll get to writing that in another article... As part of the
material I'm skipping, I'm going to breeze right over the GitLab connection and
repository information. I'm going to focus, instead, on the build operations.

1. With the new Jenkins server up and running, create a "New Item," give it a
   descriptive, memorable name, and set it as a "Freestyle Project" 

   .. image:: {attach}/images/jenkins-new-config.png
      :alt: Create a new project in Jenkins for CI.
      :width: 800 px

2. After configuring the various other settings relevant to the project (repository,
   build-triggers, etc.) find the *"Build"* section and from the *"Add build step"*
   select *"Execute shell"*.

3. In the new "Command" field of the "Execute shell" section, insert the commands
   necessary to navigate to the appropriate subdirectory and run `pytest`. In my case,
   my pytest "test folder" is located in the root directory, so I don't really need
   to change the working directory; I just go and run `pytest`. I do run a few other
   generic commands just to make sure that I've got a fair report of the build
   environment in case I need to go back and debug some things. So, here's a sample
   of what my configuration might look like.

   .. code-block:: console
   
      echo "Current Directory"
      pwd
      echo "List Folder Structure"
      ls -a ./<name-of-my-python-package-folder>
      echo "Run pytest"
      pytest -v


Summary
-------




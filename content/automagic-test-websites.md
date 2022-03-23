Title: Automagic Test Websites
Date: 2022-03-22 18:32
Modified: 2022-03-22 18:32
Tags: Youth, 4-H, Education, Jenkins, NGINX, Docker, Docker-Compose, Development, CI, CI-CD, Self-Hosted, Gitlab
Category: Youth
Slug: automagic-test-websites
Authors: Joe Stanley
Summary: Over the last few months, I've been working with a 4-H member to develop and build a smart, simple, and elegant web-application for 4-H members to upload photos they take while participating in a youth conference. Since I'm working with a 4-H member to develop the website, everything needs to have a focus on education, and I need to spend as little time as possible fussing with the infrastructure side of things, since that's not what we're focusing on. I decided that we should make a system using my self-hosted GitLab and Jenkins instances to automagically deploy changes so that the youth doesn't have to learn how that's done, and fight with the server all the time!



As you may already know, I've been working on some fun and interesting stuff with some 4-H members over the last few months. We're developing a
[Python-based photo-upload-app](/reactjs-python-pictures-and-4h.html) to allow 4-H youth (delegates) at a youth conference upload photos securely
to participate in competitions during the conference, and to share photos for the end-of-conference-slideshow.

Anyway, I'm not here to talk about the app; I'll be doing plenty more of that, I'm sure.

What I am here to talk about is how I'm making it automatically deploy the application for
[each development branch in my GitLab instance](https://gitlab.stanleysolutionsnw.com/idaho4h/4HPhotoUploader) automatically with a little Jenkins magic.
You see, since I have a personal Jenkins instance set up to work with my GitLab, it's able to authenticate and pull all of the source-code from any branch
in whichever repository I configure. Better yet, I can make it automatically look for changes to any-and-all branches, and automatically run builds when
those branches change.

What I've just described is nothing new to those who work in CI/CD (Continuous Integration/Continuous Deployment) systems, but it is valuable and, I think,
novel in this context. I'm using this automated build system to abstract the complexity of deploying a containerized application so that I can focus on
development with a youth member, and focus on programming, not deploying servers.

<embed type="text/plain" src="https://gitlab.stanleysolutionsnw.com/idaho4h/4HPhotoUploader/-/raw/develop/Jenkinsfile" width="500" height="200">
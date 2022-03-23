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

<object data="https://gitlab.stanleysolutionsnw.com/idaho4h/4HPhotoUploader/-/raw/develop/Jenkinsfile" type="text/plain"
width="500" style="height: 300px">
<a href="https://gitlab.stanleysolutionsnw.com/idaho4h/4HPhotoUploader/-/raw/develop/Jenkinsfile">No Support?</a>
</object>
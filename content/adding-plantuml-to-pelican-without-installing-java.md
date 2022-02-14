Title: Adding PlantUML to Pelican Without Installing Java?
Date: 2022-02-13 19:54
Modified: 2022-02-13 19:54
Tags: Python, Pelican, Blogging, Static-Sites, Html, Plantuml, Diagrams, Github-Actions
Category: Blogging
Slug: adding-plantuml-to-pelican-without-installing-java
Authors: Joe Stanley
Summary: We know that I don't like to do anything that computers can do for me. We also know that I like Python, and am not a huge fan of Java. So how am I going to get PlantUML integrated into my blog without actually needing to install the Java packages? Let me show you...

I've recently wanted to start adding [PlantUML](https://plantuml.com/) drawings to my blog-posts for a variety of reasons.
Trouble is, PlantUML requires Java. My blog-site is built in GitHub actions, and adding PlantUML as some kind of CLI
utility to a GitHub action sounds... well... gross!

Thankfully, I've found a way around that with the help of [`PlantUML-Markdown`](https://pypi.org/project/plantuml-markdown/),
a nice little package built to do pretty much EXACTLY what I need. It's able to shoot off the UML content to a server,
and the server hands back an image to suit my request. To demonstrate, when I use the following code-block in my markdown
article(s):

```markdown
::uml:: format="svg" classes="uml myDiagram" alt="My super diagram placeholder" title="My super diagram" width="300px" height="300px"
   !theme spacelab
   Bob->Alice : Hello!
::end-uml::
```

I, in turn, render an image such as the following:

::uml:: format="svg" classes="uml myDiagram" alt="My super diagram placeholder" title="My super diagram" width="300px" height="300px"
   !theme spacelab
   Bob->Alice : Hello!
::end-uml::

Now, to make all this work, I did need to make a few changes, and I couldn't find a clean, comprehensive set of documentation on this,
so I'm putting it together here.

-----



Title: Adding PlantUML to Pelican Without Installing Java?
Date: 2022-02-13 19:54
Modified: 2022-02-13 20:32
Tags: python, pelican, blogging, static-sites, html, plantuml, diagrams, github-actions
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
::_uml_:: format="svg" classes="uml myDiagram" alt="My super diagram placeholder" title="My super diagram" width="300px" height="300px"
   !theme spacelab
   Bob->Alice : Hello!
::end-uml::
```

*Note:* Now the auto-rendering is SO good, that I had to add underscores around the keyword `uml` in the example above. I'll do that
throughout this article in places where I *don't* want the PlantUML to actually render to an image.

I, in turn, render an image such as the following:

::uml:: format="svg" classes="uml myDiagram" alt="My super diagram placeholder" title="My super diagram" width="300px" height="300px"
   !theme spacelab
   Bob->Alice : Hello!
::end-uml::

Now, to make all this work, I did need to make a few changes, and I couldn't find a clean, comprehensive set of documentation on this,
so I'm putting it together here.

-----

I tried a number of things that didn't work, so let me just list those quickly to put them behind us:

* I'd tried using a tag directly in the uml-header to specify the server; later, I found that this option isn't even supported. So I
don't know what I was thinking!

```markdown
::_uml_:: format="svg" ... server="http://www.plantuml.com/plantuml"
```

* I then tried integrating with Pelican's PlantUML extension (which requires the Java tool be installed). I thought that I *must*
need some kind of cooperation between the two extensions... Nope. Fail.

Alright... so after trying a number of packages, and combining configurations, I finally found this little note in the PlantUML-Markdown
PyPI page:

> Then you need to specify the configuration file on the command line:
>
> `markdown_py -x plantuml_markdown -c myconfig.yml mydoc.md > out.html`

That, in turn, lead me to start thinking a bit differently.

If PlantUML can be generated with specific "global options" (i.e., the `-c myconfig.yml` portion of that command), and I can specify
which extension the `Python-Markdown` generator will run with, then I *should* be able to specify some of those configuration options
in the `pelicanconf.py` file for the Pelican site generation, right?

**Bingo.**

So... I started browsing the inter-webs, and found
[this article about fine-tuning markdown config for Pelican](https://jackdewinter.github.io/2019/10/16/fine-tuning-pelican-markdown-configuration/).
That was helpful, but left me with a few questions... So, off to the [Pelican docs](https://docs.getpelican.com/en/latest/settings.html) I went!

Lo and behold, I found that it's basically just a dictionary specifying the exact Python modules which should see certain configuration
values modified. So I did a bit of poking around to find that the `PlantUML-Markdown` module's primary file is aptly named `plantuml_markdown.py`
Taking the default `MARKDOWN` configuration dictionary provided in the Pelican documentation, I did a little modification to add the
server option I needed to let `PlantUML-Markdown` do its magic in
[my `pelicanconf.py` file](https://github.com/engineerjoe440/stanley-solutions-blog/blob/master/pelicanconf.py):

```python
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'plantuml_markdown': {                              # This line,
            'server': "http://www.plantuml.com/plantuml",   # and this one,
        },                                                  # and this one, were what I changed from the default.
    },
    'output_format': 'html5',
}
```

And of course, I added `plantuml-markdown` to [my `requires.txt` file](https://github.com/engineerjoe440/stanley-solutions-blog/blob/master/requires.txt)
so that `pip` will pull it in for the rendering.

###### Voila!

Magic, don't you think? So, hopefully this means I'll start doing a little more "drawing" in my articles.

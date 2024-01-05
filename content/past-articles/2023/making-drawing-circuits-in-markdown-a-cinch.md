Title: Making Drawing Circuits in Markdown a Cinch!
Date: 2022-08-30 13:01
Modified: 2022-08-30 13:01
Tags: markdown, pelican, blogging, circuits, schematics, python
Category: Python
Slug: making-drawing-circuits-in-markdown-a-cinch
Authors: Joe Stanley
Summary: I've talked about how someone can make PlantUML diagrams come to life, directly in markdown for blog-sites, and I've touched on other automation techniques I use to make blogs come together from plain text, but how about some circuit diagrams? Well, there wasn't a neat tool to help make this a possibility, until now!


So, wouldn't it be nice to be able to draw circuits right in your markdown? The same way that PlantUML drawings can be carved out from plain-text.

> *Sure, but that technology doesn't exist... right?*

Hah! That's what you thought...

Enter: [`schemdraw-markdown`](https://github.com/engineerjoe440/schemdraw-markdown), a brand-new tool built by yours truly that can take
[`schemdraw`](https://schemdraw.readthedocs.io/en/latest/index.html) logic embedded in special blocks of markdown and build appropriate SVG circuits to illustrate
the circuits, embedding them directly in the markdown!

I can't take all of the credit, there's some good folks who built the [`plantuml-markdown` extension](https://github.com/mikitex70/plantuml-markdown) extension,
which I've already built into my Pelican-blogsite generation, allowing me to make those awesome little drawings in some of my
[past](https://blog.stanleysolutionsnw.com/making-feline-stink-a-distant-memory.html)
[articles](https://blog.stanleysolutionsnw.com/using-python-to-provide-simple-photo-connections-for-youth.html). That tool was the starting-point for my work.
Call it inspiration; call it shameless, code-plundering; they built an excellent framework which I was able to reconfigure to support `schemdraw`. Either way,
those folks built an awesome tool, and made it really easy for me to build something similar.

## C'mon, let's show this off!

Want to see it in action? Here's a few samples:

#### The Standard Schemdraw Intro Diagram:

::schemdraw:: alt="Schemdraw Basic Diagram" color="white"
    += elm.Resistor().right().label('1Ω')
    += elm.Capacitor().down().label('10μF')
    += elm.Line().left()
    += elm.SourceSin().up().label('10V')
::end-schemdraw::

<details>
  <summary>Click to expand all the Schemdraw-Markdown Goodness!</summary>
```markdown
::_schemdraw_:: alt="My super diagram" color="white"
    += elm.Resistor().right().label('1Ω')
    += elm.Capacitor().down().label('10μF')
    += elm.Line().left()
    += elm.SourceSin().up().label('10V')
::end-schemdraw::
```
</details>


#### Something a bit Juicier:
Example [from Schemdraw Docs](https://schemdraw.readthedocs.io/en/latest/gallery/analog.html#discharging-capacitor)

::schemdraw:: alt="Analog Circuit" color="white"
    (V1 := elm.SourceV().label('5V'))
    elm.Line().right(drawing.unit*.75)
    (S1 := elm.SwitchSpdt2(action='close').up().anchor('b').label('$t=0$', loc='rgt'))
    elm.Line().right(drawing.unit*.75).at(S1.c)
    elm.Resistor().down().label('$100\Omega$').label(['+','$v_o$','-'], loc='bot')
    elm.Line().to(V1.start)
    elm.Capacitor().at(S1.a).toy(V1.start).label('1$\mu$F').dot()
::end-schemdraw::

<details>
  <summary>Click to expand all the Schemdraw-Markdown Goodness!</summary>
```markdown
::_schemdraw_:: alt="Analog Circuit" color="white"
    (V1 := elm.SourceV().label('5V'))
    elm.Line().right(drawing.unit*.75)
    (S1 := elm.SwitchSpdt2(action='close').up().anchor('b').label('$t=0$', loc='rgt'))
    elm.Line().right(drawing.unit*.75).at(S1.c)
    elm.Resistor().down().label('$100\Omega$').label(['+','$v_o$','-'], loc='bot')
    elm.Line().to(V1.start)
    elm.Capacitor().at(S1.a).toy(V1.start).label('1$\mu$F').dot()
::end-schemdraw::
```
</details>

## How Does it Work?

In a nutshell, we use some regular expressions to slurp the specially formatted section out of the markdown, and then we do some conditioning for the "instructions"
and punch them into a custom `exec` block. Yeah, that's right, the dreaded exec block. I'm not particularly pleased about it, either, but it could be worse...

> ***right?***

<img src="{attach}/images/techy-granny.jpg" width="100%" alt="Granny's got it...">

At any rate, there's no sense crying over that spilled milk, for the time-being, it's simple enough, and doesn't cause too much trouble. I clearly call out a
warning in the README docs for the new package. And speaking of the "new package," it's already on [PyPI](https://pypi.org/project/schemdraw-markdown/).

To get started with it in your documentation, just go ahead and...

```shell
$ pip3 install schemdraw-markdown
```

And let me know what you think in the comments below!

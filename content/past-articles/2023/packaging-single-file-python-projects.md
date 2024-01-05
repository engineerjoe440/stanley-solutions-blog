Title: Packaging Single File Python Projects
Date: 2023-01-16 09:50
Modified: 2023-01-16 09:50
Tags: python, packaging, pyproject.toml, pypi, development, build
Category: Python
Slug: packaging-single-file-python-projects
Authors: Joe Stanley
Summary: Somehow, I've managed to build quite a few random Python package, and contribute to others. I've recently been working towards converting all of the Python projects I manage to the new pyproject.toml standards for packaging, and I've recently had to work through an interesting little challenge for some of the projects which only contain a sigle Python file. No module folder, no `__init__.py`. Just a single file.

So... I somehow seem to have become a maintainer for a number of projects. I don't claim to be a *good* maintainer. Just that I am a maintainer. After all,
I'm involved, in one way, or another with each of the following projects.

* [`ElectricPy`](https://github.com/engineerjoe440/ElectricPy) -- I'm the Primary maintainer for this one, after all, I was the original author.
* [`PyCEV`](https://github.com/engineerjoe440/pycev) -- Again... Primary maintainer.
* [`Python-COMTRADE`](https://github.com/engineerjoe440/python-comtrade) -- Ok... so this is my fork of the original project. I'm not *quite* that clever to put this one together by myself.
* [`SELProtoPy`](https://github.com/engineerjoe440/selprotopy) -- Sole Maintainer.
* [`Schemdraw-Markdown`](https://github.com/engineerjoe440/schemdraw-markdown) -- Sole Maintainer.

Still, even *questionable* maintainers, such as myself, can exercise some good practices when it comes to package management.

## What is `pyproject.toml` and why do we care?

Good question.

It's one that lots of people have asked. So... I've put together a list of quick "finds" when I searched for *"why to move from setup.py to pyproject.toml"* on Google.

* http://ivory.idyll.org/blog/2021-transition-to-pyproject.toml-example.html
* https://stackoverflow.com/questions/72352801/migration-from-setup-py-to-pyproject-toml-how-to-specify-package-name
* https://ianhopkinson.org.uk/2022/02/understanding-setup-py-setup-cfg-and-pyproject-toml-in-python/
* https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html

There's plenty of other well-informed articles out there; I just picked the first couple. I'll rehash, though for what its worth.

The `setup.py` file is much what it sounds like. It's an executable Python file which is largely responsible for demarking the particular packaging parameters needed
for a Python project. Nothing too crazy about it, but as the industry has grown, it's become increasingly clear that having a package's installation managed in an
executable script is less than ideal.

Along came `pyproject.toml`. Offering all the same great flavors that `setup.py` brought to the table, with half the fat and fewer calories... I mean, without the
need for any executable scripts being run during installation. Bingo!

## What's so special about packaging single-file Python projects?

Well, let's look at a common Python package layout:

```
|- my_package/
|  |- __init__.py
|  |- some_other_file.py
|
|- pyproject.toml
|- setup.py
```

See that in this case, the "package" is all contained under the `my_package/` folder, which contains the appropriate `__init__.py` necessary to make the folder work
as a true Python package.

I want to do something a little *different* though. I mean, let's be honest; is it really all that surprising that I, *Joe Stanley* want to do things *differently*?

> Nope.

------

I want a flat package like the one shown below. A package that only contains a single Python file, because that's all that it needs. No extra bloatware!

```
|- my_package.py
|- pyproject.toml
|- setup.py
```

> But... How do I do that?

## Making `pyproject.toml` do my bidding...

So... after a bit of research on [`flit`'s documentation](https://flit.pypa.io/en/stable/pyproject_toml.html?highlight=tool.flit.module#module-section), and
found a nice, concise way of declaring the particular module that's available in the package. See the example below from
[my fork of `python-comtrade`](https://github.com/engineerjoe440/python-comtrade/blob/master/pyproject.toml)

```toml
[build-system]
requires = ["flit_core >=3.2,<4"]
build-backend = "flit_core.buildapi"

[project]
name = "python-comtrade"
authors = [
    {name = "David Parrini"},
    {name = "Joe Stanley", email = "engineerjoe440@yahoo.com"}
]
maintainers = [
    {name = "Joe Stanley", email = "engineerjoe440@yahoo.com"}
]
description = "A Python 3 module designed to read Common Format for Transient Data Exchange (COMTRADE) files."
readme = "README.md"
license = {file = "LICENSE"}
classifiers = [
    "License :: OSI Approved :: MIT License"
]
dynamic = ["version"]

[project.urls]
Home = "https://github.com/engineerjoe440/python-comtrade"

# Here's where the magic happens....
[tool.flit.module]
name = "comtrade"
```

And just like that... This package is ready to publish just the one little-ol'-Python-file without any heartache.

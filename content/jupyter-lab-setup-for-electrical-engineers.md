Title: Jupyter Lab Setup for Electrical Engineers
Date: 2025-03-25 06:49
Modified: 2025-03-25 06:49
Tags: calculations, jupyter, lab, notebook, python, research, study, university
Category: education
Slug: jupyter-lab-setup-for-electrical-engineers
Authors: Joe Stanley
Summary: Over the years, I've tried a few installation methods for Jupyter Notebooks and Jupyter lab. I've finally found one that I think is a little simpler than some of the others. Let me share that now for the benefit of Electrical Engineering students.

[Jupyter](https://jupyter.org/) is one of the fastest-growing exploratory tools in Python, one of the fastest-growing
languages in the early 2020's. I've used Python throughout my educational and professional career for simple calculations
all the way up to complex operational control systems. While I won't claim Python is the best-suited tool for every
application. It's my first go-to. If it won't work for something, I will often find that quicker in Python, and I'll be
directed to the "right tool" for that particular job. Just like in spoken and written languages, there's often a language
particularly well-suited for each application.

Jupyter is a framework which allows scientists, engineers, researchers, and others to quickly dive into the Python space
with great power and efficiency. It provides a clean web-interface for individuals and teams to work together on projects,
and is now recommended by a number of resources for engineers.

- [*Why Every Data Engineer Needs Jupyter* -Tim Webster (**Art of Data Engineering**)](https://artofdataengineering.com/why-every-data-engineer-needs-jupyter/)
- [*10 Reasons Why Data Scientists Love Jupyter Notebooks* -Aarthi Kumaraswamy (**Packt**)](https://www.packtpub.com/en-us/learning/how-to-tutorials/10-reasons-data-scientists-love-jupyter-notebooks/)
- [*Jupyter Notebooks for Chemical Engineering Education* -Jeffrey C. Kantor (**University of Notre Dame**)](https://cache.org/sites/default/files/S19-Jupyter-Notebooks.pdf)

I've come to enjoy Jupyter for use with electrical engineering work for many of the same reasons that scientists and
researchers enjoy it. Code cells right next to documentation cells makes for a truly wonderful and simple pairing.

I'm not really here to sell you on Jupyter as a tool, however. I'm really here to describe what I feel is becoming the
best way to install Jupyter, to date.

---

With Python's evolving landscape of package managers, [`pipx`](https://pipx.pypa.io/latest/) has come to be my "go-to-tool"
for command-line applications both big and small. I won't go into great length about what it is and isn't, but I'll say
that it makes it possible to install great command-line applications in Python without dependency conflicts or disrupting
any system-level packages.

> Now, to cut to the chase...

#### 1. Install `pipx`

Pipx is not a default package that's included with Python installations. So that's the first thing we'll need to install.
I could give specific directions, but instead, I'll refer you directly to [their thorough documentation](https://pipx.pypa.io/latest/installation/).
Follow their guide to getting pipx installed.

I anticipate that many electrical engineers who might be reading this will be working with Windows. That does make things
ever so slightly trickier. I'd recommend that if you're running Windows, just use Python's `pip` (the regular one) to
do the installation for you.

```shell
python -m pip install --user pipx
```

> ℹ️ **NOTE:**
>
> This assumes something important...
>
> It assumes that Python is already part of your Windows path. If it's not, or you run the command above and see an error
> about "python could not be found" (or something similar), then you'll need to add Python to your path. For the sake of
> brevity here, I'll point you towards [another great article](https://realpython.com/add-python-to-path/) showing
> information on that.

#### 2. Installing Jupyter Lab with `pipx`

This is, perhaps, the easiest part. Just run the following command and let pipx do all of the work!

```shell
pipx install jupyterlab --include-deps
```

#### 3. Install Jupyter Notebook with Jupyter Lab (so you have both)

I like to have both `jupyter notebook` and `jupyter lab` installed because for different use-cases, I use the different
applications. The following command will install the notebook server right alongside the lab server. This makes it really
easy to start either.

```shell
pipx inject jupyterlab notebook
```

#### 4. Add other Numerical Libraries

While we're at it, we might as well install some of the common Python numerical libraries. Things like `numpy`, or `scipy`
are, perhaps, most common. At the risk of becoming a shameless, self-promoter. Why don't we install
[`electricpy`](https://electricpy.readthedocs.io/en/latest/); the Python package I began maintaining in 2018 which
contains all manner of electrical-engineering formulas. Luckily for us, it *depends* on those other numerical libraries,
so when we install `electricpy`, they'll come along for the ride!

```shell
pipx inject jupyterlab electricpy
```

#### 5. Profit!

As the "cool kids" like to say, it's time to profit off the efforts, now. Go ahead! Open a terminal and issue the
following command, you should see Jupyter Notebook spring to life in your browser and get right into it!

```shell
jupyter notebook
```

Notice that when you ran that command, the session in your browser started up in the same folder... This means that
wherever your terminal is running when you start `jupyter notebook` or `jupyter lab`, that's where the browser session
will also start. By extension, you can see how you'd be able to open or work with any file just by navigating to that
directory in your terminal. For guides on that, take a look at the following articles.

- [*CMD: 11 basic commands you should know (cd, dir, mkdir, etc.)* -Codrut Neagu (**Digital Citizen**)](https://www.digitalcitizen.life/command-prompt-how-use-basic-commands/)
- [*30 Bash Commands Cheat Sheet* -Bosko Marijan (**Phoenix NAP**)](https://phoenixnap.com/kb/bash-commands)

---

Now get out there, and engineer something awesome!

Title: Automating Python Releases with GitHub Actions
Date: 2021-11-25 14:01
Modified: 2021-11-25 14:01
Tags: Automation, Python, Github Actions, PyPI
Category: Python
Slug: automating-python-releases-with-github-actions
Authors: Joe Stanley
Summary: I'm pretty lazy... We've covered that already, but wouldn't it be exceptionally nice if I could make GitHub automate Python package releases for me? Lets do that...


Oh yes. I'm lazy.

Haven't we established that, yet? Well, we're going to hit that nail home with this topic...

We've established previously that I manage a number of random Python packages, including *ElectricPy*, *SELProtoPy*, and *PyCEV*.
I've come to the realization that I need all the help I can get with releasing updates on a regular basis. So... How shall we do
that?

### Where to Start?

I decided that I needed this for *ElectricPy* first. So let's start with figuring out what we want to do:

* Identify the Current ElectricPy Version from the Source Code (bail out if the version is the same or older than what's previously been released)
* Create a Tag that Matches the ElectricPy Version, then Push that to GitHub
* Build the Python Package as a Source-Code Bundle, and as a [Python Wheel](https://pythonwheels.com)
* Push the Packages to the Python Package Index (PyPI)

So those are the primary requirements. Now, let's work out how we're going to do it. I know that I want to use GitHub actions to
do this whole thing. So let's start there.

### What are GitHub Actions, Anyway?

Well, GitHub actions are GitHub's way of providing CI/CD systems. Essentially, providing Linux-container based workflows that are
defined through YAML description files. The YAML (which stands for Yet Another Mark-up Language) files define what container base
should be used, and what the steps need to be completed.

### Are there any Read-to-Go GitHub Actions?

Well, yes... But, actually no.

There's quite a few pretty good actions available in the community, but getting everything *just* right is a bit more tricky. Why, you
ask? Well, they all completed one or two of those actions I'd outlined above, but they didn't cover the whole list. So, I decided to
glue them all together with a bit of Python!

### Start by Identifying the Version

We need to pick the version out of the ElectricPy package, and then we need to double-check that it's not already used, or older than
the most-up-to-date version. So I built a simple little script:

```python
# Release Versioning Support Script
# Joe Stanley | 2021

import requests

USERNAME = 'engineerjoe440'
REPO = 'electricpy'

try:
    import electricpy as ep
except ImportError:
    import os, sys
    sys.path.insert(0, os.getcwd())
    import electricpy as ep

import requests

response = requests.get(f"https://api.github.com/repos/{USERNAME}/{REPO}/releases/latest")
try:
    latest = response.json()["name"]
except Exception:
    latest = '0.0.0'

# Verify Version is Newer
version = f"v{ep._version_}"
if version <= latest:
    raise ValueError("Module version is not newer than previous release!")
else:
    print(version)
```

So, that script does a couple things for us. It polls GitHub for the latest release marked in the repo under my
username and project name. It then verifies that the version is valid and *new*.

### How About that Action Definition?

So, we've covered one of the four pieces we need to accomplish. What's left? Well, we still need to build the
Python package (but that's easy) and then create the release and push it to PyPI. Lucky for us, both of those
remaining "questions" there's ready-made GitHub actions! So what does this whole thing look like?

```yml
name: Release
on:
  push:
   branches:
     - master

jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      # https://github.com/marketplace/actions/setup-python
      # ^-- This gives info on matrix testing.
      - name: Install Python
        uses: actions/setup-python@v1
        with:
          python-version: "3.10"
      - name: Identify Version
        id: version
        run: |
          python -m pip install requests build --user
          python -m pip install -r requirements.txt --user
          output=$(python release-version.py)
          echo "::set-output name=version::$output"
      - name: Build Artifacts
        if: success()
        id: build
        run: |
          python -m build --sdist --wheel --outdir dist/
      - name: Create Release
        uses: ncipollo/release-action@v1
        with:
          tag: ${{ steps.version.outputs.version }}
          name: Release ${{ steps.version.outputs.version }}
          body: ${{ steps.tag_version.outputs.changelog }}
          artifacts: "dist/*"
      - name: Publish distribution 📦 to PyPI
        if: success()
        uses: pypa/gh-action-pypi-publish@master
        with:
            password: ${{ secrets.PYPI_API_TOKEN }}
```

That big definition basically does a bunch of stuff for us; I'll break it out by each of the steps:

1. Check out the source code.
2. Install Python 3.10 - Because we kinda need that. Notice here that `3.10` is in double quotes as: "3.10".
That's because otherwise, the GitHub system might mistake it as 3.1... You know, because 3.10 is really just
a decimal number with an extra 0 at the end.
3. Use the Python Script (from above) to figure out the version. But not before installing the required
packages; both for the script, and for *ElectricPy*.
4. Build the Artifacts - The things we want to keep. Namely the source-code distribution (`--sdist`) and the
wheel file.
5. Create the GitHub release. This will place the package on the GitHub repo's "Releases" page and add a new
tag to the repository so it's easy to back-track the code.
6. Finally, push those artifacts to PyPI so they're available for download and install with `pip`.


### Wrapping Up

This might not be the biggest accomplishment, but it's a huge relief because it makes automating releases
and pushing out updates MUCH easier. So, let's bring on the new features and updates!!!


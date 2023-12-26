Title: Adding Search to my Pelican Blog Site
Date: 2023-12-26 11:45
Modified: 2023-12-26 11:45
Tags: Blog, Search, Python, Stork, Static-Site
Category: Python
Slug: adding-search-to-my-pelican-blog-site
Authors: joestan
Summary: I'm quickly approaching the mark of 50 blog posts, which is wonderful! But it also means that finding that "thing" I wrote some time ago is becoming an increasing challenge. So... I need to add search to my blog site. But how? It's a static site, after all, there's not really a "backend" to do the search functionality for me... Luckily, there's some wonderful folks who've written tooling to add just this functionality. Here's how I added it to my blog site!

Search is never easy, right? Especially when we're adding it to a static website, which by its very definition does not have any server-side tools to
permit the construction of some form of server index, and live searching capability.

So how do we do it?

*With Javascript, of course!*

... wait ... that sounds kinda awful for somebody who's a Python fan through-and-through.

Thank goodness there's some tools out there, already that make this all possible!

---

<img src="{attach}/images/stanley-solutions-blog-search.png" style="width: 40%; margin: 10px;" alt="Behold! Search..." align="right">

## Introducing: [`pelican-search`](https://pypi.org/project/pelican-search/)

As the name implies, this Pelican plugin incorporates search capabilities into a Python [*Pelican*](https://getpelican.com/)-based system. Simply put,
at the time of generation, the plugin indexes all of the content in the blog's many pages and puts together one big "cheat-sheet" from which a few Javascript
utilities may pull references to support a search functionality. The end product looks like what I've shown here, on the right.

Pelican Search relies heavily on [Stork Search](https://stork-search.net/), a Rust-powered
(*insert audio effect from [Jupiter Broadcasting](https://www.jupiterbroadcasting.com/) here...*) search tool that markets itself as:

> Impossibly fast web search, made for static sites.

I started working on this a few months ago, in a little "free time" (basically non-existent for me these days), and didn't have much success.
Most notably, my current system was not using a `<main>...</main>` tag to contain the body of the page as is
[documented in their repository](https://github.com/pelican-plugins/search?tab=readme-ov-file#stork-html-selector), and although I'd tried a few of their
other incantations, nothing was quite working as I needed.

To further complicate things, my primary Pelican theme ([`Pelican-Alchemy`](https://github.com/nairobilug/pelican-alchemy/tree/master)), was being loaded
into my project simply by installing the tarball, directly from GitHub. This meant that although I was pulling the most-up-to-date source, it wasn't
available directly in my blog's repository.

So... There's my first task. Remove the tarball from my `requirements.txt` file and make `Pelican-Alchemy` a proper git submodule in my project.

```diff
pelican
- https://github.com/nairobilug/pelican-alchemy/tarball/master
Markdown
plantuml-markdown
schemdraw-markdown
```

> [*source*](https://github.com/engineerjoe440/stanley-solutions-blog/commit/69ec5d9c17c009db95154cde95855c096c469232#diff-4d7c51b1efe9043e44439a949dfd92e5827321b34082903477fd04876edb7552L2)

And in case you're wondering, I just needed to run the following command to add the package as a git submodule:

```shell
git submodule add https://github.com/nairobilug/pelican-alchemy themes/pelican-alchemy
```

A little editing in my `pelicanconf.py` file, later, and I was now ready to use the submodule-style theme.

```diff
- import alchemy
- THEME = alchemy.path()
+ THEME = 'themes/pelican-alchemy/alchemy'
THEME_TEMPLATES_OVERRIDES = ['content/templates']
BOOTSTRAP_CSS = 'https://bootswatch.com/4/darkly/bootstrap.css'
THEME_CSS_OVERRIDES = [
```

> [*source*](https://github.com/engineerjoe440/stanley-solutions-blog/commit/69ec5d9c17c009db95154cde95855c096c469232#diff-d65cf0288f1d9a86915f40ad4e588bbbb59fd7b1f932ea9beaa39927e3bcf18c)

Oh! and don't forget that we need to use submodules when we do the checkout in GitHub actions!

```diff
    name: Build
    runs-on: ubuntu-latest
    steps:
-      - uses: actions/checkout@v2
+      - name: Checkout
+        uses: actions/checkout@v4
+        with:
+          submodules: true
      - name: Install Python
        uses: actions/setup-python@v1
        with:
```

> [*source*](https://github.com/engineerjoe440/stanley-solutions-blog/commit/69ec5d9c17c009db95154cde95855c096c469232#diff-38c69d4be1b4265f1a6d512ddf513406b8ab04ce80c69d55c88bb945f5e0aa49)

Now... with the full source of `Python-Alchemy` in my repo, I got to some spelunking...

<img src="{attach}/images/commit-doge-such-wow.png" style="width: 30%; margin: 10px;" alt="Behold! Search..." align="left">

> I've just got to stop and show you this. While I was poking around in there, I saw this commit message... Just look at this thing.
>
> Glorious.

Anyway...

I started poking around, and found that if I over-rode the `article.html` Jinja template, I could add the `<main>...</main>` that I so
desperately wanted. So, I did! I added a new file called `article.html` to my `content/templates/` directory. This file was almost an
exact copy of the original Alchemy template, with the addition of the `main` tag as shown here.

```diff
...
{% endblock %}

{% block content %}
+  <main>
    <article class="article">
      <header>
...
      </div>
    </article>
+  </main>
  {% include 'include/comments.html' %}
{% endblock %}
```

> [*source*](https://github.com/engineerjoe440/stanley-solutions-blog/commit/69ec5d9c17c009db95154cde95855c096c469232#diff-6b66599ff6ea4101dd39c64fe73d90e190fea2325620fc0ea1dbb477f12a6b4b)



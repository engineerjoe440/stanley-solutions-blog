Title: Adding a Subscription System to my Blog
Date: 2024-01-04 20:52
Modified: 2024-01-04 20:52
Tags: blog, website, html, python, pelican, jinja2, static-site, mailing-list, listmonk, email, newsletter
Category: Blogging
Slug: adding-a-subscription-system-to-my-blog
Authors: Joe Stanley
Summary: I've finally gotten around to getting some basic configurations with my Listmonk mailing list system going. I got started with configurations for the Idaho 4-H Roundup podcast (did I mention I've started a podcast?), but now I'm also getting one started for my blog site. Here's how I added the HTML to get it working here.

Okay, so really there isn't much to this. I ended up needing to do some troubleshooting, but most of that was because of my own misunderstanding.
Ultimately, with my [Pelican-Alchemy](https://github.com/nairobilug/pelican-alchemy) theme, there's an option to add a list of the direct templates which
should be rendered as HTML pages for the Pelican site. After enough monkeying around, I found this option, and added my new `subscribe` option.

```python
# Default value is ['index', 'tags', 'categories', 'authors', 'archives']
DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'authors', 'archives', 'subscribe']
```

That `subscribe` corresponds to the new `subscribe.html` file that I stored in my
[`content/templates/`](https://github.com/engineerjoe440/stanley-solutions-blog/tree/master/content/templates) folder. That file is actually pretty simple:

```html
{% extends "base.html" %}

{% block title %}
  Subscribe {{ super() }}
{% endblock %}

{% block page_header %}
  Subscribe
{% endblock %}

{% block content %}
  <form method="post" action="{{ LISTMONK_URL }}" class="listmonk-form">
    <div>
        <h3>{{ SITENAME }} Newsletter</h3>
        <input type="hidden" name="nonce" />
        <p><input type="email" class="stork-input" name="email" required placeholder="E-mail" /></p>
        <p><input type="text" class="stork-input" name="name" placeholder="Name (optional)" /></p>
      
        <p>
          <input hidden id="8a08b" type="checkbox" name="l" checked value="{{ LISTMONK_LIST_ID }}" />
        </p>
        
        <p><input type="submit" value="Subscribe" class="btn btn-success btn-lg" /></p>
    </div>
  </form>
{% endblock %}
```

You can see that I made some customizing tweaks to allow me to use variables for the Listmonk URL and List ID. Those end up landing in the
`pelicanconf.py` file:

```python
LISTMONK_URL = "https://listmonk.stanleysolutionsnw.com"
LISTMONK_LIST_ID = "8a08bea9-66e2-4b36-9140-17f303bda981"
```

With the final addition to my customized `footer.html` as shown below, I'm up and running with a new subscribe page on the ol' website!

```diff
      <li class="list-inline-item"><a href="{{ SITEURL }}/{{ TAGS_URL or TAGS_SAVE_AS or 'tags.html' }}">Tags</a></li>
    {% endif %}
+    <li class="list-inline-item"><a href="{{ SITEURL }}/{{ SUBSCRIBE_URL or SUBSCRIBE_SAVE_AS or 'subscribe.html' }}">Subscribe</a></li>
  {% else %}
```

<img src="{attach}/images/add-subscription-to-blog.png" style="width: 100%" alt="Making Subscribing WAY Easier">

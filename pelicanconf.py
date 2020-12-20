#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Joe Stanley'
SITENAME = 'Stanley Solutions Blog'
SITEURL = 'https://engineerjoe440.github.io/stanley-solutions-blog/'

import alchemy, pygments_solarized
THEME = alchemy.path()
BOOTSTRAP_CSS = 'https://bootswatch.com/4/darkly/bootstrap.css'
SITESUBTITLE = 'Engineering and creativity - all under one hat.'
PYGMENTS_STYLE = pygments_solarized.dark
SITEIMAGE = 'logo.png'
DESCRIPTION = ('Electrical Engineering blog by Joe Stanley - Python,' + 
    'Python3, IEC 61131-3, Industrial Controllers, Real-Time Control')

PLUGINS=[
    'sitemap',
]

SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.5,
        "indexes": 0.5,
        "pages": 0.5
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "daily",
        "pages": "monthly"
    }
}

PATH = 'content'
STATIC_PATHS = [
    'images',
    'pdfs',
    'extra',
    'html',
]

EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'custom.css'},
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},  # and this
    'extra/logo.png':    {'path': 'logo.png'},
    'extra/CNAME': {'path': 'CNAME'},
    'extra/LICENSE': {'path': 'LICENSE'},
    'extra/README': {'path': 'README'},
    'html/google307ea14d75106813.html': {'path': 'google307ea14d75106813.html'},
}
ARTICLE_EXCLUDES = [
    'html'
]

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/{slug}.rss.xml'
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Joe On GitHub', 'https://github.com/engineerjoe440/'),
         ('ElectricPy Project', 'https://engineerjoe440.github.io/ElectricPy/'),
         ('KRNC Project', 'https://github.com/engineerjoe440/KRNCApps/'),
         ('SELProtoPy Project', 'https://engineerjoe440.github.io/sel-proto-py'),
         ('PyCEV Project', 'https://engineerjoe440.github.io/pycev'),
         ('RSS Feed', 'feeds/all.rss.xml'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
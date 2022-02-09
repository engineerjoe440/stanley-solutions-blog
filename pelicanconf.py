#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import os

AUTHOR = 'Joe Stanley'
SITENAME = 'Stanley Solutions Blog'
SITEURL = 'https://engineerjoe440.github.io/stanley-solutions-blog/'

import alchemy
THEME = alchemy.path()
THEME_TEMPLATES_OVERRIDES = ['content/templates']
BOOTSTRAP_CSS = 'https://bootswatch.com/4/darkly/bootstrap.css'
THEME_CSS_OVERRIDES = [
    '/custom.css'
]
SITESUBTITLE = 'Engineering and creativity - all under one hat.'
PYGMENTS_STYLE = 'monokai'
SITEIMAGE = 'logo.png'
DESCRIPTION = ('Electrical Engineering blog by Joe Stanley - Python,' + 
    'Python3, IEC 61131-3, Industrial Controllers, Real-Time Control')

ISSO_URL = "https://blogcomments.stanleysolutionsnw.com"

PLUGINS=[
    'render_math',
    'pelican_photos',
    'sitemap',
]

PHOTO_LIBRARY = os.path.join(os.getcwd(), "content", "images")
PHOTO_WATERMARK = False

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
    'html',
    'templates'
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
         ('SELProtoPy Project', 'https://engineerjoe440.github.io/selprotopy'),
         ('PyCEV Project', 'https://engineerjoe440.github.io/pycev'),
         ('KRNC Project', 'https://github.com/engineerjoe440/KRNCApps/'),
         ('Calendar', 'https://calendar.google.com/calendar/u/0?cid=ZW5naW5lZXJqb2U0NDBAZ21haWwuY29t'),
         ('RSS Feed', 'feeds/all.rss.xml'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

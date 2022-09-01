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
    'photos',
    'sitemap',
]

PHOTO_LIBRARY = os.path.join(os.getcwd(), "content", "images")
PHOTO_GALLERY = (2048, 1024, 80)
PHOTO_WATERMARK = False
PHOTO_SQUARE_THUMB = False
PHOTO_RESIZE_JOBS = -1
PHOTO_INLINE_GALLERY_ENABLED = True
PHOTO_INLINE_GALLERY_TEMPLATE = "inline_gallery"

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'plantuml_markdown': {
            'server': "http://www.plantuml.com/plantuml",
        },
        'schemdraw_markdown': {},
    },
    'output_format': 'html5',
}

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
LINKS = (('Stanley Solutions Website', 'https://stanleysolutionsnw.com'),
         ('GitHub', 'https://github.com/engineerjoe440/'),
         ('GitLab', 'https://gitlab.stanleysolutionsnw.com/engineerjoe440'),
         ('Gitea', 'https://gitea.stanleysolutionsnw.com/engineerjoe440'),
         ('ElectricPy Project', 'https://electricpy.readthedocs.io/en/latest/'),
         ('SELProtoPy Project', 'https://engineerjoe440.github.io/selprotopy'),
         ('PyCEV Project', 'https://engineerjoe440.github.io/pycev'),
         ('KRNC Project', 'https://github.com/engineerjoe440/KRNCApps/'),
         ('Calendar', 'https://calendar.google.com/calendar/embed?src=engineerjoe440%40gmail.com&ctz=America%2FLos_Angeles'),
         ('RSS Feed', 'feeds/all.rss.xml'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

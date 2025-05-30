#!/usr/bin/env python
# -*- coding: utf-8 -*- #
################################################################################
"""
Stanley Solutions Blog Site Configuration

Building:

    pelican -s pelicanconf.py --fatal errors


Local Development and Testing:

    pelican -s pelicanconf.py -l -r
"""
################################################################################
import os

AUTHOR = 'Joe Stanley'
SITENAME = 'Stanley Solutions Blog'
if os.getenv("GITHUB_ACTIONS") is not None:
    # Running GitHub Actions
    SITEURL = 'https://blog.stanleysolutionsnw.com'
else:
    SITEURL = 'localhost:8000'
    RELATIVE_URLS = True


THEME = 'themes/pelican-alchemy/alchemy'
THEME_TEMPLATES_OVERRIDES = ['content/templates']
BOOTSTRAP_CSS = 'https://bootswatch.com/4/darkly/bootstrap.css'
THEME_CSS_OVERRIDES = [
    '/custom.css',
    'https://files.stork-search.net/dark.css'
]
SITESUBTITLE = 'engineering and creativity - all under one hat'
PYGMENTS_STYLE = 'monokai'
SITEIMAGE = 'logo.png'
DESCRIPTION = ('Electrical Engineering blog by Joe Stanley - Python,' + 
    'Python3, IEC 61131-3, Industrial Controllers, Real-Time Control')

ISSO_URL = "https://blogcomments.stanleysolutionsnw.com"

LISTMONK_URL = "https://listmonk.stanleysolutionsnw.com"
LISTMONK_LIST_ID = "8a08bea9-66e2-4b36-9140-17f303bda981"

PLUGINS=[
    'render_math',
    'photos',
    'sitemap',
    'search',
]

PHOTO_LIBRARY = os.path.join(os.getcwd(), "content", "images")
PHOTO_GALLERY = (2048, 1024, 80)
PHOTO_WATERMARK = False
PHOTO_SQUARE_THUMB = False
PHOTO_RESIZE_JOBS = -1
PHOTO_INLINE_GALLERY_ENABLED = True
PHOTO_INLINE_GALLERY_TEMPLATE = "inline_gallery"

MARKDOWN = {
    'extensions': [
        'customblocks',
    ],
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

HIDE_AUTHORS = True

PATH = 'content'
STATIC_PATHS = [
    'images',
    'pdfs',
    'extra',
    'html',
]

DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'authors', 'archives', 'subscribe']

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
LINKS = (
    ('Stanley Solutions Website', 'https://stanleysolutionsnw.com'),
    ('ElectricPy', 'https://electricpy.readthedocs.io/en/latest/'),
    ('SELProtoPy', 'https://engineerjoe440.github.io/selprotopy'),
    ('PyCEV', 'https://engineerjoe440.github.io/pycev'),
    ('KRNC Barn Manager', 'https://gitlab.stanleysolutionsnw.com/krnc/usb-manager'),
    ('Schemdraw-Markdown', 'https://github.com/engineerjoe440/schemdraw-markdown'),
    ('WordWall', 'https://github.com/engineerjoe440/wordwall'),
)

# Icons
ICONS = (
    ('fas fa-comments', 'https://matrix.to/#/@engineerjoe440:stanleysolutionsnw.com'),
    ('github', 'https://github.com/engineerjoe440/'),
    ('gitlab', 'https://gitlab.stanleysolutionsnw.com/engineerjoe440'),
    ('fas fa-coffee', 'https://gitea.stanleysolutionsnw.com/engineerjoe440'),
    ('fas fa-calendar', 'https://calendar.google.com/calendar/embed?src=engineerjoe440%40gmail.com&ctz=America%2FLos_Angeles'),
    ('rss', 'feeds/all.rss.xml'),
)

DEFAULT_PAGINATION = 10


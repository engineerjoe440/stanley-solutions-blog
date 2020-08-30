#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Joe Stanley'
SITENAME = 'Stanley Solutions Blog'
SITEURL = 'https://engineerjoe440.github.io/stanley-solutions-blog/'

import alchemy
THEME = alchemy.path()
BOOTSTRAP_CSS = 'https://bootswatch.com/4/darkly/bootstrap.css'
SITESUBTITLE = 'Engineering and creativity - all under one hat.'
SITEIMAGE = 'logo.png'
DESCRIPTION = ('Electrical Engineering blog by Joe Stanley - Python,' + 
    'Python3, IEC 61131-3, Industrial Controllers, Real-Time Control')

PATH = 'content'
STATIC_PATHS = ['images',
                'pdfs',
                'extra']

EXTRA_PATH_METADATA = {
    #'extra/custom.css': {'path': 'custom.css'},
    #'extra/robots.txt': {'path': 'robots.txt'},
    '{attach}/extra/favicon.ico': {'path': 'favicon.ico'},  # and this
    #'extra/logo.png':    {'path': 'logo.png'}
    #'extra/CNAME': {'path': 'CNAME'},
    #'extra/LICENSE': {'path': 'LICENSE'},
    #'extra/README': {'path': 'README'},
}

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_RSS = 'feeds/all.rss.xml'
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Joe On GitHub', 'https://github.com/engineerjoe440/'),
         ('ElectricPy Project', 'https://engineerjoe440.github.io/ElectricPy/'),
         ('KRNC Project', 'https://github.com/engineerjoe440/KRNCApps/'),
         ('RSS Feed', 'feeds/all.rss.xml'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
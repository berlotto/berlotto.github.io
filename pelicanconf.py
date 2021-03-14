#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Sérgio Berlotto'
SITENAME = 'Programador Livre'
SITEURL = 'localhost:8000'

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'pt_BR'

CC_LICENSE='CC-BY-SA'
CC_LICENSE_DERIVATIVES = "yes"
CC_LICENSE_COMMERCIAL = "yes"
CC_ATTR_MARKUP = True

FAVICON = 'static/favicon.ico'

# https://github.com/gilsondev/pelican-clean-blog
THEME = 'themes/pelican-clean-blog'
STATIC_PATHS=[
    'static',
]

# - THEME CONFIGURATION
HEADER_COVER = 'static/homecover-1.jpg'
# HEADER_COLOR = 'black'
SHOW_SOCIAL_ON_INDEX_PAGE_HEADER=True
CSS_OVERRIDE = 'static/custom.css'
# - THEME CONFIGURATION


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Author profile', 'https://github.com/berlotto'),
)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/sergioberlotto'),
          ('github', 'https://github.com/berlotto'),
          ('facebook','https://facebook.com/sergio.berlotto'),
          ('linkedin','https://www.linkedin.com/in/sergioberlotto'),
          ('telegram','https://t.me/sergioberlotto'))

DEFAULT_PAGINATION = False
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
OUTPUT_PATH = 'docs/'

# https://github.com/pelican-plugins/seo
SEO_REPORT = True 
SEO_ENHANCER = True
SEO_ENHANCER_OPEN_GRAPH = True

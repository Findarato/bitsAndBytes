#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Joseph Harry'
SITENAME = u'Joe Code'
SITEURL = ''

PATH = 'content'
LOAD_CONTENT_CACHE = False


TIMEZONE = 'America/Chicago'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
USE_FOLDER_AS_CATEGORY = True

#Plugins
PLUGINS = [
    'encrypt_content',
    'gravatar',
    'goodreads_activity',
    'events',
    'image_process',
    'pelican_githubprojects',
    'pelican-open_graph',
    'pelican_youtube'
]

ENCRYPT_CONTENT = {
    'title_prefix': '[Encrypted]',
    'summary': 'This content is encrypted.'
}
# Blogroll
LINKS = (
    ('WPL','https://wpl.lib.in.us'),
    ('Pelican', 'http://getpelican.com/'),
    ('Python.org', 'http://python.org/'),
    ('Jinja2', 'http://jinja.pocoo.org/'),
    ('You can modify those links in your config file', '#')
)

# Social widget
SOCIAL = (('Github', 'https://github.com/findarato'),
          ('Google plus', 'https://plus.google.com/102630360601349400454/about'),
          ('Twitter', 'https://twitter.com/findarato88'))

DEFAULT_PAGINATION = 5

DEFAULT_METADATA = {
    'status': 'draft',
}
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

PYGMENTS_RST_OPTIONS = {'classprefix': 'pgcss', 'linenos': 'table'}


#THEME = "themes/materialistic-pelican"
#THEME = "themes/pelican-material"
THEME = "themes/blue-penguin"

# all defaults to True.
DISPLAY_HEADER = True
DISPLAY_FOOTER = True
DISPLAY_HOME   = True
DISPLAY_MENU   = True

# provided as examples, they make ‘clean’ urls. used by MENU_INTERNAL_PAGES.
TAGS_URL           = 'tags'
TAGS_SAVE_AS       = 'tags/index.html'
AUTHORS_URL        = 'authors'
AUTHORS_SAVE_AS    = 'authors/index.html'
CATEGORIES_URL     = 'categories'
CATEGORIES_SAVE_AS = 'categories/index.html'
ARCHIVES_URL       = 'archives'
ARCHIVES_SAVE_AS   = 'archives/index.html'

# use those if you want pelican standard pages to appear in your menu
MENU_INTERNAL_PAGES = (
    ('Tags', TAGS_URL, TAGS_SAVE_AS),
    ('Authors', AUTHORS_URL, AUTHORS_SAVE_AS),
    ('Categories', CATEGORIES_URL, CATEGORIES_SAVE_AS),
    ('Archives', ARCHIVES_URL, ARCHIVES_SAVE_AS),
)

# additional menu items
#MENUITEMS = (
#    ('GitHub', 'https://github.com/'),
#    ('Linux Kernel', 'https://www.kernel.org/'),
#)

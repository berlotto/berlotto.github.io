from datetime import datetime

AUTHOR = "Alexandre Vicenzi"
SITEURL = "http://localhost:8000"
SITENAME = 'Programador Livre'
SITETITLE = 'Programador Livre'
SITESUBTITLE = "Informações para programadores"

SITEDESCRIPTION = "Flex - The minimalist Pelican theme."

SITELOGO = '/static/logo.png'
FAVICON = 'static/favicon.ico'
BROWSER_COLOR = "#333333"

PYGMENTS_STYLE = "monokai"

ROBOTS = "index, follow"

THEME = '/home/sergio/Desenvolvimento/pelican-themes/Flex'
PATH = "content"
OUTPUT_PATH = "blog/"
TIMEZONE = 'America/Sao_Paulo'

DISABLE_URL_HASH = True

PLUGIN_PATHS = ['/home/sergio/Desenvolvimento/pelican-plugins']

SEO_REPORT = True 
SEO_ENHANCER = True
SEO_ENHANCER_OPEN_GRAPH = True

PLUGINS = ['i18n_subsites','post_stats', 'neighbors', 'related_posts']

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

I18N_TEMPLATES_LANG = "pt"
DEFAULT_LANG = 'pt_BR'
OG_LOCALE = "pt_BR"
LOCALE = "pt_BR.utf8"

DATE_FORMATS = {
    "pt": "%B %d, %Y",
}

GOOGLE_GLOBAL_SITE_TAG="G-P8RS2G0QCD"
GOOGLE_GTAG="G-P8RS2G0QCD"

FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = True

SOCIAL = (
    ('twitter', 'https://twitter.com/sergioberlotto'),
    ('github', 'https://github.com/berlotto'),
    ('facebook','https://facebook.com/sergio.berlotto'),
    ('linkedin','https://www.linkedin.com/in/sergioberlotto'),
    ('telegram','https://t.me/sergioberlotto'),
)

MENUITEMS = (
    ("Archives", "/archives.html"),
    ("Categories", "/categories.html"),
    ("Tags", "/tags.html"),
)

CC_LICENSE = {
    "name": "Creative Commons Attribution-ShareAlike 4.0 International License",
    "version": "4.0",
    "slug": "by-sa",
    "icon": True,
    "language": "en_US",
}

COPYRIGHT_YEAR = datetime.now().year
DEFAULT_PAGINATION = 10

DISQUS_SITENAME = "berlottogithubio"

STATIC_PATHS=[
    'static',
]

THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

USE_LESS = True

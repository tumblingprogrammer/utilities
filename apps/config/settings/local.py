
from .base import *

DEBUG = True

MIDDLEWARE_CLASSES += (
    'livereload.middleware.LiveReloadScript',
)
INSTALLED_APPS += [
    'livereload',
]
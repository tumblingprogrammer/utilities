import os
import environ
from manage import get_env_variable
DJANGO_SECRET_KEY = get_env_variable('DJANGO_SECRET_KEY')
SECRET_KEY = DJANGO_SECRET_KEY

ROOT_DIR = str(environ.Path(__file__) - 4)
APPS_DIR = str(os.path.join(ROOT_DIR,'apps'))
TEMPLATES_DIR = str(os.path.join(APPS_DIR,'templates'))
STATIC_DIR = str(os.path.join(APPS_DIR,'static'))
MEDIA_ROOT = str(os.path.join(APPS_DIR,'media'))
DATABASE_FILE_NAME = str(os.path.join(APPS_DIR,'db.sqlite3'))
STATIC_ROOT = str(os.path.join(ROOT_DIR,'staticfiles'))
MEDIA_URL = '/media/'
STATICFILES_DIRS = [STATIC_DIR, ]

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
THIRD_PARTY_APPS = [
]
LOCAL_APPS = [
    'main',
]
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)
ROOT_URLCONF = 'config.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            TEMPLATES_DIR,
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
WSGI_APPLICATION = 'config.wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': DATABASE_FILE_NAME,
    }
}
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = '/static/'
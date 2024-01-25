from pathlib import Path
import os
import dj_database_url
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-gd5_^^lzj_**vigtk04o9rl^58h%diiabig72fo(3#40*!6e(@'

DEBUG = True

ALLOWED_HOSTS = ['https://dress-shop-g9lx.onrender.com', 'http://127.0.0.1:8000/']

# SECURE_HSTS_SECONDS = 60 * 60 * 24 * 365

# SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# SECURE_HSTS_PRELOAD = True

# SECURE_SSL_REDIRECT = True

# SESSION_COOKIE_SECURE = True

# CSRF_COOKIE_SECURE = True

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
    'django.contrib.humanize',
    'easy_thumbnails',
    'django_cleanup.apps.CleanupConfig',    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'project.wsgi.application'

if DEBUG == True:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

else:
    DATABASES = {
        "default": dj_database_url.parse(os.environ.get("DATABASE_URL"))
    }


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en'

TIME_ZONE = 'Asia/Almaty'

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"
STATICFILES_DIRS = ["static"]

# MEDIA_ROOT = ["media"]
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = "media/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

THUMBNAIL_ALIASES = {
    '': {
        'profile': {'size': (600, 600)},
        'lenta': {'size': (300, 300)},
    },
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'medet20231020@gmail.com'
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")

# LOGGING = {
#     'version':1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'file': {
#             'level':'INFO',
#             'class': 'logging.FileHandler',
#             'filename': os.path.join(BASE_DIR, 'debug.log'),
#         },
#         'smtp': {
#             'level':'ERROR',
#             'class':'logging.handlers.SMTPHandler',
#             'mailhost':"smtp.gmail.com",
#             'credentials': ('medet20231020@gmail.com', 'spvy wsbs xblp ewch'),
#             'secure':(),
#             'fromaddr':'medet20231020@gmail.com',
#             'toaddrs':['medet20231020@gmail.com'],
#             'subject': 'Application Error',
#             'formatter': 'simple',
#         },
#     },
#     'formatters': {
#         'simple': {
#             'format': '[%(asctime)s] %(levelname)s: %(message)s',
#             'datefmt': '%Y.%m.%d %H:%M:%S'
#         }
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['file', 'smtp'],
#             'level': 'DEBUG',
#             'propogate': True,
#         },
#     },
# }
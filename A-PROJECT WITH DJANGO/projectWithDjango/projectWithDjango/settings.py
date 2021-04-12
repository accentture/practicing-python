"""
Django settings for projectWithDjango project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'a@k)e=q0s!mby7z(b9x12o4m^7_na2m@j7ilm9b4fo&t$27j!7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',



    #adding app of ckeditor
    'ckeditor',
    'mainapp',
    'pages.apps.PagesConfig', #to make configurations in administration panel and charging app
    'blog.apps.BlogConfig'
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

ROOT_URLCONF = 'projectWithDjango.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # charging my context_processors
                'pages.context_processors.get_pages',
                'blog.processor.get_categories'
            ],
            
        },
    },
]

WSGI_APPLICATION = 'projectWithDjango.wsgi.application'







# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

""" 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
} 
"""


#doing configuration for database
DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'projectdjango', #name of database created in django
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT':3306
    }
}
"""
    to install a driver to run between python to connect django with mysql
        py -m pip install mysqlclient


    --if the installatin doesn't work go in google to python libraries uci
    --or go to this url: https://www.lfd.uci.edu/~gohlke/pythonlibs/
    --after search mysqlclient and click

    --check version and features of python
        py --version
        py (64 bits for example) 

    --to exectue migrations
        py manage.py migrate

"""





# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'es-es' # configurating language in spanish

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

# ================== configurations to upload image
MEDIA_URL = '/media/' # indiccating what is name where will be saved multimedia files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # specifying path of this media file
                                      # BASE_DIR : base directory of the project    
                                      # media : name of de folder




# to change toolbar of ckeditor
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink'],
            ['RemoveFormat', 'Source', 'Table', 'Image'] # Table : to add otpion of table to toolbar
                                                         # Image : to add otpion of image to toolbar
        ]
    }
}









""" 
        # =========================== ENRICHED TEXT (CKEDITOR)
        --to add enriched text in pages from administration panel, these acts as a little word in administration panel
            1. tiny mce
            2. ckeditor

        --to install ckeditor in django
            py -m pip install django-ckeditor

        --to check documentation fo ckeditor : https://django-ckeditor.readthedocs.io/en/latest/
    """
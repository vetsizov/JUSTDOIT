"""
Django settings for todoapp project.

Generated by 'django-admin startproject' using Django 2.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""
'''settings.py содержит различные настройки для нашего проекта'''
import os
import django_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
'''DEBUG это булевая переменная, которая отвечает за подробности выводимой информации.
Она полезна когда вы ищете ошибку, но в "живом" режиме её лучше отрубать.'''
DEBUG = True

'''ALLOWED_HOSTS это список адресов, с которых сервер готов принимать подключения.
Когда мы работаем в отладочном режиме, эта переменная игнорируется.
В других случаях сервер сравнивает запрос, который к нему приходит и проверяет,
что он идёт именно по тому адресу, на который он отвечает. Это сделано для дополнительной безопасности работы проекта.'''
ALLOWED_HOSTS = []


# Application definition
'''INSTALLED_APPS указывает, какие из приложений используются в проекте.
По умолчанию там только основные джанговские элементы, используемые в большинстве случаев:
django.contrib.admin это приложение для администрирования проекта
django.contrib.auth используется для авторизации пользователей
django.contrib.contenttypes подключен для поддержки различных форматов отдоваемого контента (json/картинка/текст/html)
django.contrib.sessions используют для сохранения сессий пользователя между заходами
django.contrib.messages это приложение для высвечивания информации пользователю в зависимости от его действий
django.contrib.staticfiles это специальное приложения для раздачи статики (js/css)'''
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tasks.apps.TasksConfig', #добавили приложение для работы со списком дел
    'accounts.apps.AccountsConfig', #приложение для аккаунтов пользователей
]

'''MIDDLEWARE это список используемых "прослоек",
которые применяются для каждого запроса последовательно,
от момента начала работы с ним, до момента как это приходит в код проекта'''
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

'''ROOT_URLCONF это строковая переменная, указывающая,
в какой модуль надо смотреть чтобы начать разбираться, за какие пути отвечают какие функции в коде'''
ROOT_URLCONF = 'todoapp.urls'

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

WSGI_APPLICATION = 'todoapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
'''DATABASES это, как можно понять, настройка доступа к базе'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static"),] #чтобы все видели папку static в корне проекта

LOGIN_REDIRECT_URL = "tasks:list" #при вводе логина загрузить список дел

MEDIA_URL = "/media/" # путь в вебе для медиаданных (чтобы правильно работали картинки)
MEDIA_ROOT = os.path.join(BASE_DIR, "media") # где сами эти файлы искать в системе

#настройка почты для отправки писем
#EMAIL_HOST = os.environ.get("EMAIL_HOST")                       #хост для SMTP-сервера. Если не задан, то считается что это localhost
#EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")             #логин для SMTP-сервера
#EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")     #пароль для SMTP-сервера
#EMAIL_PORT = int(os.environ.get("EMAIL_PORT"))                  #порт для SMTP-сервера; по умолчанию 25
#EMAIL_USE_TLS = bool(os.environ.get("EMAIL_USE_TLS"))           #EMAIL_USE_TLS и EMAIL_USE_SSL: булевые флаги для настроек безопасности

#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' #вывод писем в консоль вместо SMTP-серверая настроек безопасности


django_heroku.settings(locals())
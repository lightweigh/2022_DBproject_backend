"""
Django settings for DjangoProject project.

Generated by 'django-admin startproject' using Django 4.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import datetime
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-7s&+c)-vxndgcv1$y+qzocg+19bmwo(12tub0#=+!b7xt^r+ac'

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

    'rest_framework.authtoken',
    'django_filters',
    'corsheaders',
    'rest_framework',
    'app01.apps.App01Config'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # 添加1，注意中间件的添加顺序
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 支持跨域配置开始
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

ROOT_URLCONF = 'DjangoProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [],
        'DIRS': [os.path.join(BASE_DIR, 'front/dist')]
        ,
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

# AUTH_USER_MODEL = 'app01.MerchantOrUser'		# 重写原有的用户model类

WSGI_APPLICATION = 'DjangoProject.wsgi.application'

REST_FRAMEWORK = {
    # 权限  ->  - 已经登陆认证的用户可以对数据进行增删改操作，没有登陆认证的只能查看数据。
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'rest_framework_jwt.authentication.JSONWebTokenAuthentication', # 配置验证方式为JWT
        # 'rest_framework.authentication.TokenAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework.authentication.BasicAuthentication',
        'app01.auth.CsrfExemptSessionAuthentication',
    ],

    # 全局配置分页选项
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 2,

    # 过滤器的默认配置
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
}

# JWT_AUTH = {
#     'JWT_EXPIRATION_DELTA': datetime.timedelta(days=3),  # 过期时间为3
#     'JWT_AUTH_HEADER_PREFIX': 'JWT',  # Token 的头为：JWT xxxxxxxxx
#     'JWT_ALLOW_REFRESH': False,  # 不允许刷新
# }

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
MEDIA_ROOT = os.path.join(BASE_DIR, 'upload/')
MEDIA_URL = '/upload/'  # 这个是在浏览器上访问该上传文件的url的前缀

# todo 把默认的sqllite3数据库换成我们的mysql数据库
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_hw',
        'USER': 'root',
        'PASSWORD': 'NXGvdnjJbjJS6879',  # 原来那个太难记了
        # 'PASSWORD': 'kll1225', # 原来那个太难记了
        'HOST': '127.0.0.1',
        'PORT': 3306,  # 不要这个嘛？
        'OPTIONS': {
            "init_command": "SET default_storage_engine='INNODB'"
        }
    }
}
DATABASES['default']['OPTIONS']['init_command'] = "SET sql_mode='STRICT_TRANS_TABLES'"  # 排除错误
# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Add for vuejs
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "front/dist/static"),
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

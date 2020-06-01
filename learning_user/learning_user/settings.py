import os
from . import ms

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR,'templates')
TEMPLATE2_DIR = os.path.join(BASE_DIR,'mybasic_app/templates')


STATIC_DIR = os.path.join(BASE_DIR,'static')
STATIC2_DIR = os.path.join(BASE_DIR,'mybasic_app/static')

MEDIA_DIR = os.path.join(BASE_DIR,'media')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*0(9h2)vlgn0ig)fy5#827o2@*dr=%f$%s*3&^j1^x78+qx1nf'

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
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    'django.contrib.humanize',
    'django_filters',
    'crispy_forms',
    'ckeditor',
# ++++++++++++++   des Appliaction +++++++++++++++++
    'mybasic_app',              # >>>>>  principe de site >> article corrige >> poste et ttt
    'accounts',                       #All  Control par admin
    'Poste_By_Admin',  #pour searching et voir les Doc qui poste by admin 
    'Contact_Info_Adminstration',     # hnaa ga3 swalhe li ytpostoo ml 3nde admin
    'G__evaluation' # +++ hadii  les mth t3 t9samme  + evaluation 
     
     
 
]


CRISPY_TEMPLATE_PACK = 'bootstrap4'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]

ROOT_URLCONF = 'learning_user.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR,TEMPLATE2_DIR],
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


WSGI_APPLICATION = 'learning_user.wsgi.application'
ASGI_APPLICATION = 'learning_user.Asgi.application'




# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
]





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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [

STATIC_DIR,STATIC2_DIR
]


MEDIA_URL = '/media/'


MEDIA_ROOT = MEDIA_DIR





###################################################################################


AUTH_USER_MODEL = 'mybasic_app.User'


LOGIN_REDIRECT_URL='LoginByProfile'
LOGOUT_REDIRECT_URL='/'






##############

EMAIL_HOST=ms.EMAIL_HOST
EMAIL_PORT =ms.EMAIL_PORT
EMAIL_HOST_USER = ms.EMAIL_HOST_USER
EMAIL_HOST_PASSWORD=ms.EMAIL_HOST_PASSWORD



EMAIL_USE_TLS=True
EMAIL_USE_SSL=False


# +++  hadi bach save les email w t3refe chkon resle w ga3 les deatiles f folder(sent_emails) 
EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = os.path.join(BASE_DIR, "sent_emails")



from django.contrib.messages import constants as messages




# Messages built-in framework jayin f bootstrap 

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-secondary',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}



#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'width': '500px',
        'height': '10%',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList'],

        ],
    }
}


CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"

APP_DIR = os.path.join(BASE_DIR, 'accounts')
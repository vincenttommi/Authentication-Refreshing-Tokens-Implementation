from pathlib import Path
from datetime import timedelta



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-z!^u963b7129#opx@#=a+txmj4a_+9h(cpmk*0v9k_badm9q)l'

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
    'base',
    'rest_framework',
    'rest_framework_simplejwt.token_blacklist'
]

REST_FRAMEWORK = {
   
    'DEFAULT_AUTHENTICATION_CLASSES': (
        
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
   
}


SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
    # A datetime.timedelta object which specifies how long access tokens are vali
    "REFRESH_TOKEN_LIFETIME": timedelta(days=90),
    # A datetime.timedelta object which specifies how long refresh tokens are validalue is added to the current UTC time during token generation to obtain the token’s default “exp” claim value.
    "ROTATE_REFRESH_TOKENS": True,
    #When set to True, if a refresh token is submitted to the TokenRefreshView, a new refresh token will be returned along with the new access token. 
    "BLACKLIST_AFTER_ROTATION": True,
    # When set to True, causes refresh tokens submitted to the TokenRefreshView to be added to the blacklist if the blacklist app is in use and the ROTATE_REFRESH_TOKENS setting is set to True
    "UPDATE_LAST_LOGIN": False,
    #When set to True, last_login field in the auth_user table is updated upon login
    "ALGORITHM": "HS256",
    #The algorithm from the PyJWT library which will be used to perform signing/verification operations on tokens
    "VERIFYING_KEY": "",
    # The verifying key which is used to verify the content of generated tokens
    "AUDIENCE": None,
    # The audience claim to be included in generated tokens and/or validated in decoded tokens. When set to None, this field is excluded from tokens and is not validated
    "ISSUER": None,
    #The issuer claim to be included in generated tokens and/or validated in decoded tokens
    "JSON_ENCODER": None,
    
    "JWK_URL": None,
    # The JWK_URL is used to dynamically resolve the public keys needed to verify the signing of tokens
    "LEEWAY": 0,
    #Leeway is used to give some margin to the expiration time 

    "AUTH_HEADER_TYPES": ("Bearer",),
    #The authorization header type(s) that will be accepted for views that require authentication 
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    # The authorization header name to be used for authentication. The default is HTTP_AUTHORIZATION which will accept the Authorization header in the request
    "USER_ID_FIELD": "id",
    # The database field from the user model that will be included in generated tokens to identify users
    "USER_ID_CLAIM": "user_id",
    # The claim in generated tokens which will be used to store user identifiers
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",
    # Callable to determine if the user is permitted to authenticate
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
        # A list of dot paths to classes that specify the types of token that are allowed to prove authentication
    "TOKEN_TYPE_CLAIM": "token_type",
    # The claim name that is used to store a token’s type
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",
    #A stateless user object which is backed by a validated token. 
    "JTI_CLAIM": "jti",
    #The claim name that is used to store a token’s unique identifier. 
    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),

    "TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainPairSerializer",
    "TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSerializer",
    "TOKEN_VERIFY_SERIALIZER": "rest_framework_simplejwt.serializers.TokenVerifySerializer",
    "TOKEN_BLACKLIST_SERIALIZER": "rest_framework_simplejwt.serializers.TokenBlacklistSerializer",
    "SLIDING_TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainSlidingSerializer",
    "SLIDING_TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSlidingSerializer",
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

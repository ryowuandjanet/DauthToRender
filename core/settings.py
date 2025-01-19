from pathlib import Path
import dj_database_url

from environ import Env
env=Env()
Env.read_env()

ENVIRONMENT = env('ENVIRONMENT',default="production")


BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = env('SECRET_KEY')

if ENVIRONMENT == 'development':
    DEBUG = True
else:
    DEBUG = False

SECRET_KEY = "django-insecure-5dh)0gi2$j&y^2ayz^jlnv*)1l&yi32n9rri4d6tw)-ae931ga"

DEBUG = True

ALLOWED_HOSTS = []

INTERNAL_IPS={
    '127.0.0.1',
    'localhost:3000',
    'solid-broccoli-p5x5qr75gqc67q5-3000.app.github.dev'
}

CSRF_TRUSTED_ORIGINS = ['https://dauthtorender.onrender.com']

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.sites", 
    "django.contrib.staticfiles",
    'cloudinary_storage',
    'cloudinary',
    'allauth',
    'allauth.account',
    'yfcase',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR/'templates'],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"

AUTHENTICATION_BACKENDS = [

    # 這是 Django 的默認身份驗證後端。
    #   它通過數據庫中的 User 模型來驗證用戶憑據。
    #   支持基於用戶名和密碼的身份驗證。
    #   提供以下功能：
    #       超級用戶 (is_superuser) 可繞過所有權限檢查。
    #       支持基於群組和用戶權限的檢查。
    'django.contrib.auth.backends.ModelBackend',
    # 這是 Django Allauth 提供的身份驗證後端。
    # 它擴展了默認的身份驗證後端，支持更豐富的功能，例如：
    #   電子郵件作為登錄憑據（如果在 Allauth 配置中啟用）。
    #   支持社交帳號（如 Google、Facebook 等）的身份驗證。
    #   整合電子郵件驗證機制。
    # 通常用於需要更靈活的身份驗證系統或集成社交登錄的項目。
    'allauth.account.auth_backends.AuthenticationBackend',

]

if ENVIRONMENT == 'development':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': dj_database_url.parse(env('DATABASE_URL'))
    }

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
STATICFILES_DIRS = [ BASE_DIR / 'static' ]
STATIC_ROOT=BASE_DIR /'staticfiles'

MEDIA_URL = 'media/'

if ENVIRONMENT == 'development':
    MEDIA_ROOT = BASE_DIR / 'media' 
else:
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
    CLOUDINARY_STORAGE={
        'CLOUDINARY_URL': env('CLOUDINARY_URL')
    }

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# settings.py
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST='smtp.gmail.com'
EMAIL_HOST_USER=env('EMAIL_ADDRESS')
EMAIL_HOST_PASSWORD=env('EMAIL_HOST_PASSWORD')
EMAIL_PORT=587
EMAIL_USE_TLS=True
DEFAULT_FROM_EMAIL=f"Django App Name {env('EMAIL_ADDRESS')}"
ACCOUNT_EMAIL_SUBJECT_PREFIX=''

# settings.py

# 啟用電子郵件驗證
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'  # 可選值: "none", "optional", "mandatory"
ACCOUNT_EMAIL_REQUIRED = True             # 強制要求用戶在註冊時提供電子郵件

# 登錄前強制驗證電子郵件
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = False

# 註冊成功後重定向到的 URL
ACCOUNT_SIGNUP_REDIRECT_URL = '/accounts/confirm-email/'

# 可選：設置電子郵件發送後的確認頁面
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = '/accounts/login/'
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = '/'

# 登錄後重定向的 URL，設為根 URL
LOGIN_REDIRECT_URL = '/'

# 登出後重定向的 URL，可選設為根 URL
ACCOUNT_LOGOUT_REDIRECT_URL = '/'

# 可選：如果希望登錄頁面本身也是根 URL，可以設置
ACCOUNT_LOGIN_ON_PASSWORD_RESET = True

# 確保 Django 使用正確的站點 URL
SITE_ID = 1
LOGOUT_REDIRECT_URL = '/accounts/login/'

# 使用的協議 (http 或 https)
ACCOUNT_DEFAULT_HTTP_PROTOCOL = "https"

# 發送電子郵件時使用的默認域名
DEFAULT_FROM_EMAIL = "ryowu0329@gmail.com"  # 替換為您自己的電子郵件




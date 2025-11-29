import os
from pathlib import Path
import dj_database_url
from dotenv import load_dotenv

# --------------------------------
# PATHS
# --------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# --------------------------------
# ENVIRONMENT
# --------------------------------
# DEBUG debe venir desde Render (variable DEBUG=False)
DEBUG = os.getenv("DEBUG", "False") == "True"

# Cargar .env solo en desarrollo local
if DEBUG and os.path.exists(BASE_DIR / ".env"):
    load_dotenv()

# --------------------------------
# SECRET KEY
# --------------------------------
SECRET_KEY = os.getenv("SECRET_KEY", "fallback-secret-key")

# --------------------------------
# ALLOWED HOSTS
# --------------------------------
ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    os.getenv("RENDER_EXTERNAL_HOSTNAME", ""),   # Render autogenera host
]

RENDER = os.environ.get('RENDER', None)

# Agregar el hostname generado automáticamente por Render
if RENDER:
    hostname = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
    if hostname:
        ALLOWED_HOSTS.append(hostname)
        
# --------------------------------
# APPS
# --------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',

    'api',
    'tasks'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'tareas.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'tareas.wsgi.application'

# --------------------------------
# DATABASE
# --------------------------------
# Render te provee DATABASE_URL automáticamente
DATABASES = {
    "default": dj_database_url.config(
        default="postgres://tareas_db:administrador@localhost:5432/tareas_dbp",
        conn_max_age=600,
    )
}

# Require SSL solo en producción
if not DEBUG:
    DATABASES["default"]["OPTIONS"] = {"sslmode": "require"}

# --------------------------------
# PASSWORD VALIDATION
# --------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# --------------------------------
# TIMEZONE
# --------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Bogota'
USE_I18N = True
USE_TZ = True

# --------------------------------
# STATIC FILES
# --------------------------------
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

# --------------------------------
# REST FRAMEWORK
# --------------------------------
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticated",
    ),
    "UNAUTHENTICATED_USER": None,
}

# --------------------------------
# CORS
# --------------------------------
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True

import dj_database_url
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret key (mantenha isso seguro e fora do código fonte!)
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-i+z1h+_e&coxi!%_%b5#*&&8cy^@y*c9+$wfb0hr2xnoqyw%&^')

# Debug deve ser False no ambiente de produção
DEBUG = os.getenv('DEBUG', 'False') == 'True'

# Allowed hosts para produção
ALLOWED_HOSTS = ['seu-app-no-render.onrender.com', 'limamotos.com.br']

# Static files para Render
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Whitenoise para servir arquivos estáticos
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # outros middlewares...
]

# Banco de dados
DATABASES = {
    'default': dj_database_url.config(default='postgres://limamotos_db_user:IsltuyMnD6EwZFY4XZlwivGWFudh0maI@dpg-cv49l7ofnakc73bkvqqg-a/limamotos_db')
}

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # outras apps...
]

# Password validation
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

# Internacionalização
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Configuração de arquivos estáticos
STATIC_URL = 'static/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# WSGI application
WSGI_APPLICATION = 'limamotos.wsgi.application'

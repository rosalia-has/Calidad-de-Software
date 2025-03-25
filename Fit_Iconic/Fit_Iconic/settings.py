import os
from pathlib import Path

# Definir el directorio base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-4zz@!8-@92**%&!k%=#hfg53k+=m@c9o5+xob@g@3wcxcb+vxe'

# Para desarrollo, se recomienda tener DEBUG en True
DEBUG = True  # O False si estás en producción

# Configura los hosts permitidos, en desarrollo puedes usar 'localhost' y '127.0.0.1'
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']  # Para desarrollo, puedes agregar aquí más dominios en producción
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Puedes cambiar a PostgreSQL o MySQL si usas otro motor
        'NAME': BASE_DIR / 'db.sqlite3',  # Nombre de la base de datos
    }
}


INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
    'users',  # Nuestra app personalizada de usuarios
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOW_ALL_ORIGINS = True  # Permitir peticiones desde cualquier origen

# Configuración de archivos estáticos
STATIC_URL = '/static/'

# Configuración de plantillas
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Ruta donde pondrás tus plantillas
        'APP_DIRS': True,  # Buscará plantillas dentro de las apps si no se encuentra en la ruta especificada
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

# Archivo de URLs raíz
ROOT_URLCONF = 'Fit_Iconic.urls'

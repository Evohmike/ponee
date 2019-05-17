from .base import *  # noqa
from .base import env


DEBUG = True
SECRET_KEY = env('SECRET_KEY')
ALLOWED_HOSTS = ['localhost', '0.0.0.0', '127.0.0.1']
CORS_ORIGIN_ALLOW_ALL = True
EMAIL_BACKEND = env(
    "EMAIL_BACKEND",
    default="django.core.mail.backends.console.EmailBackend"
)
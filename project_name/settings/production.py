from .base import *  # noqa
from .base import env
import django_heroku

ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS")
CORS_ORIGIN_WHITELIST = env.list(
    'CORS_ORIGIN_WHITELIST',
    default=[]
)
SECURE_SSL_REDIRECT = True

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}

EMAIL_HOST = env('EMAIL_HOST')
EMAIL_PORT = env('EMAIL_PORT')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_USE_SSL = True

django_heroku.settings(locals())
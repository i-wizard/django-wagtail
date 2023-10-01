from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-rk2ab14nlhv#0p4g-6ne66%!l@8q5($ajmfs!+dct3xn%l1+sh"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
# INSTALLED_APPS.append("debug_toolbar")
# MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")
#
# INTERNAL_IPS = ("127.0.0.1",)

try:
    from .local import *
except ImportError:
    pass

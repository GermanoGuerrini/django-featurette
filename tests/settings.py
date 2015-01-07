from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test',
    }

}
ROOT_URLCONF = 'urls'
SITE_ID = 1
INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django_featurette',
)

TEMPLATE_CONTEXT_PROCESSORS += ("django.core.context_processors.request",)

SECRET_KEY = 'sk'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)
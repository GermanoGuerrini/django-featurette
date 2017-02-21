import os

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

SECRET_KEY = 'sk'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'DIRS': [
            os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates'),
        ],
         'OPTIONS': {
                'context_processors': [
                    'django.core.context_processors.request',
                ],
            },
    },
]
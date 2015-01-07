from setuptools import setup, find_packages

APP_NAME = 'django_featurette'

setup(
    name=APP_NAME,
    version="%s.%s" % __import__(APP_NAME).VERSION[:2],
    packages=find_packages(),
    include_package_data=True,
    description = 'Features for selected users',
    author = 'Germano Guerrini',
    author_email = 'germano.guerrini@gmail.com',
    url = 'https://github.com/GermanoGuerrini/django-featurette',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
)

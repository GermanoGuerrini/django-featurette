===========
Usage
===========

The first thing to do is to create one instance of
:py:class:`Feature <django_featurette.models.Feature>` for each feature you want
to implement.

Basically, a feature is simply an arbitrary key that can be associated to a `Group`
of users (the way Django intends it) and is active over a certain time window.

To create a new feature just use the supplied admin interface. The same goes for
the group and the relative users, given that you installed the admin provided by Django.

Now, let's say we have an active feature identified by the key `premium_feature`.
Let's examine the three way you can use that to show some given content only to
users within the group associated to the feature.

Decorate a view
===============

If that's what your feature requires, you can return an `HttpResponseForbidden`
instead of the normal response of a view using a decorator:

.. code-block:: python

    from django_featurette.decorators import user_enabled

    @user_enabled('premium_feature')
    def premium_view(request):
        [your code goes here]


Using a template tag
====================

If you just need to hide some content from a template, you can use a template tag:

.. code-block:: html+django

    {% load featurette %}
    
    {% feature premium_feature %}
    You can see this because we love you
    {% endfeature %}

Fine-grained control
====================

As a last resource, you can use an helper method to control your view flow (or
other methods that handles users):

.. code-block:: python

    from django_featurette.utils import is_feature_enabled_for_user

    def get_premium(user):
        gift = '1 dollar'
        if is_feature_enabled_for_user('premium_feature', user):
            gift = '10 dollars'
        return gift

That's all!
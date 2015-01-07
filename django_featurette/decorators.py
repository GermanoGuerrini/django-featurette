from django.http import HttpResponseForbidden

from django_featurette.utils import is_feature_enabled_for_user

def user_enabled(feature_key):
    """
    Decorator to check whether the current user can access the feature or not,
    in order to block the whole view function.
    """
    def wrap(view):
        def wrapped_view(*args):
            # request is always the first parameter of a django view
            user = args[0].user
            if is_feature_enabled_for_user(feature_key, user):
                return view(*args)
            else:
                return HttpResponseForbidden('<h1>Access Denied</h1>')
        return wrapped_view
    return wrap
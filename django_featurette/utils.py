import datetime

from django_featurette.models import Feature

def get_enabled_features_for_user(user):
    """
    Returns a list of features enabled for the current authenticated user.
    If the user can't access any feature or is anonymous, returns an empty list.
    """
    enabled_features = []
    if user.is_authenticated():
        now = datetime.datetime.now
        enabled_features = Feature.objects.filter(is_active=True,
            start_date__lte=now, end_date__gte=now,
            group__in=user.groups.all())
    return enabled_features

def is_feature_enabled_for_user(feature_key, user):
    """
    Returns True if a certain feature is enabled for a user.
    Usefull for a fine-grained control inside a view function.
    If no feature exists with the given key, it returns False.
    """
    try:
        feature = Feature.objects.get(key=feature_key)
        return feature in get_enabled_features_for_user(user)
    except Feature.DoesNotExist:
        return False

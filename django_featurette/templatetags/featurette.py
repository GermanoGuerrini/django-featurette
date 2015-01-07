from django import template

from django_featurette.utils import is_feature_enabled_for_user

register = template.Library()

@register.tag('feature')
def do_feature(parser, token):
    """
    Outputs the contents of the block if the feature passed as argument is
    enabled for the currently authenticated user.

    Example:

    .. code-block:: html+django

        {% load featurette %}
        {% feature my_feature_key %}
            You get this because you have been
            selected among billion of users
        {% endfeature %}
    """
    nodelist = parser.parse(('endfeature',))
    parser.delete_first_token()
    tokens = token.contents.split()
    if len(tokens) != 2:
        error = "%r tag requires a feature key argument." % tokens[0]
        raise template.TemplateSyntaxError(error)
    return FeatureNode(nodelist, tokens[1])


class FeatureNode(template.Node):
    def __init__(self, nodelist, feature_key):
        self.nodelist = nodelist
        self.feature_key = feature_key

    def render(self, context):
        try:
            user = context['request'].user
            if is_feature_enabled_for_user(self.feature_key, user):
                return self.nodelist.render(context)
            return ''
        except KeyError:
            return ''
        
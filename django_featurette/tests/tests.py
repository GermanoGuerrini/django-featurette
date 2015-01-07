import datetime

from django.test import SimpleTestCase
from django.test import RequestFactory
from django.contrib.auth import models
from django.core.urlresolvers import reverse
from django.template import Template, Context, TemplateSyntaxError

from django_featurette.models import Feature
from django_featurette.utils import (
    get_enabled_features_for_user,
    is_feature_enabled_for_user
)

class FeaturetteTest(SimpleTestCase):

    def setUp(self):
        self.user_a = models.User.objects.create_user(
            username='walter',
            email='w@a.com',
            password='pwd')
        self.user_b = models.User.objects.create_user(
            username='jesse',
            email='j@a.com',
            password='pwd'
        )
        self.group_a = models.Group.objects.create(name='group_a')
        self.group_b = models.Group.objects.create(name='group_b')
        self.group_a.user_set.add(self.user_a)
        self.group_b.user_set.add(self.user_b)
        self.feature_a = Feature.objects.create(
            key='feature_a',
            group=self.group_a,
            start_date=datetime.datetime(2000,1,1),
            end_date=datetime.datetime(2000,2,1),
            is_active=False,
        )
        self.feature_b = Feature.objects.create(
            key='feature_b',
            group=self.group_b,
            start_date=datetime.datetime.now() - datetime.timedelta(days=1),
            end_date=datetime.datetime.now() + datetime.timedelta(days=1),
            is_active=True,
        )

    def tearDown(self):
        self.user_a.delete()
        self.user_b.delete()
        self.group_a.delete()
        self.group_b.delete()
        self.feature_a.delete()
        self.feature_b.delete()

    def test_anonymous_get_enabled_features_for_user(self):
        self.assertItemsEqual(get_enabled_features_for_user(self.user_a), [])

    def test_logged_1_get_enabled_features_for_user(self):
        self.client.login(username='walter', password='pwd')
        self.assertItemsEqual(get_enabled_features_for_user(self.user_a), [])
        self.client.logout()

    def test_logged_2_get_enabled_features_for_user(self):
        self.client.login(username='jesse', password='pwd')
        self.assertItemsEqual(get_enabled_features_for_user(self.user_b), [self.feature_b])
        self.client.logout()

    def test_is_feature_enabled_for_user(self):
        self.assertFalse(is_feature_enabled_for_user('feature_a', self.user_a))
        self.assertFalse(is_feature_enabled_for_user('feature_b', self.user_a))
        self.assertFalse(is_feature_enabled_for_user('feature_a', self.user_b))
        self.assertTrue(is_feature_enabled_for_user('feature_b', self.user_b))

    def test_decorator_for_anonymous_user(self):
        url = reverse('test_feature_a')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)

        url = reverse('test_feature_b')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)

        url = reverse('test_feature_c')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)

    def test_decorator_for_authenticated_user_a(self):
        self.client.login(username='walter', password='pwd')

        url = reverse('test_feature_a')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)

        url = reverse('test_feature_b')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)

        url = reverse('test_feature_c')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)

        self.client.logout()

    def test_decorator_for_authenticated_user_b(self):
        self.client.login(username='jesse', password='pwd')

        url = reverse('test_feature_a')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)

        url = reverse('test_feature_b')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        url = reverse('test_feature_c')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)

        self.client.logout()

    def test_template_tag_for_anonymous_user(self):
        template = Template("""
            {% load featurette%}
            {% feature feature_b %}
            Ok
            {% endfeature %}
        """)
        rendered = template.render(Context({}))
        self.assertEqual(rendered.strip(), '')

    def test_template_tag_for_authenticated_user(self):
        template = Template("""
            {% load featurette%}
            {% feature feature_b %}
            Ok
            {% endfeature %}
        """)
        factory = RequestFactory()
        request = factory.get('/')
        request.user = self.user_b
        rendered = template.render(Context({'request': request}))
        self.assertEqual(rendered.strip(), 'Ok')

    def test_template_tag_for_authenticated_user_but_no_features(self):
        template = Template("""
            {% load featurette%}
            {% feature feature_a %}
            Ok
            {% endfeature %}
        """)
        factory = RequestFactory()
        request = factory.get('/')
        request.user = self.user_b
        rendered = template.render(Context({'request': request}))
        self.assertEqual(rendered.strip(), '')

    def test_template_tag_no_args(self):
        with self.assertRaises(TemplateSyntaxError):
            template = Template("""
                {% load featurette%}
                {% feature %}{% endfeature %}
            """)
            template.render(Context({}))

    def test_template_tag_too_many_args(self):
        with self.assertRaises(TemplateSyntaxError):
            template = Template("""
                {% load featurette%}
                {% feature feature_a feature_b %}{% endfeature %}
            """)
            template.render(Context({}))
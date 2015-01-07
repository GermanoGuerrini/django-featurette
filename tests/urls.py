from django.conf.urls import patterns, url

urlpatterns = patterns('django_featurette.tests.views',
    url(r'^test_feature_a/', 'test_feature_a', name="test_feature_a"),
    url(r'^test_feature_b/', 'test_feature_b', name="test_feature_b"),
    url(r'^test_feature_c/', 'test_feature_c', name="test_feature_c"),
)
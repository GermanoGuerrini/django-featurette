from django.conf.urls import url

from django_featurette.tests import views


urlpatterns = [
    url(r'^test_feature_a/', views.test_feature_a, name="test_feature_a"),
    url(r'^test_feature_b/', views.test_feature_b, name="test_feature_b"),
    url(r'^test_feature_c/', views.test_feature_c, name="test_feature_c"),
]
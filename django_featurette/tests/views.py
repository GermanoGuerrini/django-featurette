from django.http import HttpResponse

from django_featurette.decorators import user_enabled

@user_enabled('feature_a')
def test_feature_a(request):
    return HttpResponse('ok')

@user_enabled('feature_b')
def test_feature_b(request):
    return HttpResponse('ok')

@user_enabled('feature_c')
def test_feature_c(request):
    return HttpResponse('ok')
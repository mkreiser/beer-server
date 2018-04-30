from django.conf.urls import url
from django.contrib.auth import views as django_views

from rest_framework.urlpatterns import format_suffix_patterns

from beerApp import views

urlpatterns = [
  url(r'^$', views.api_root),

  url(r'^beers/$', views.BeerGETAll.as_view()),
  url(r'^beers/pourBeer/(?P<pk>[0-9]+)/$', views.BeerGET.as_view()),
  url(r'^beers/brewBeer/$', views.BeerPOST.as_view()),
  url(r'^beers/mixBeer/(?P<pk>[0-9]+)/$', views.BeerPUT.as_view()),
  url(r'^beers/tossBeer/(?P<pk>[0-9]+)/$', views.BeerDELETE.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

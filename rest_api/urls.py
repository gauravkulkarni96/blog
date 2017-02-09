from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^api/$', views.postList.as_view()),
    url(r'^api/(?P<pk>\d+)/$', views.postDetail.as_view()),
]

url = format_suffix_patterns(urlpatterns)
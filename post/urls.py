from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from .views import *


urlpatterns = [
	url(r'^$', post_list, name='list'),
	url(r'^create/$', post_create, name='create'),
	url(r'^(?P<id>\d+)/', post_detail, name='detail'),
	url(r'^delete/(?P<id>\d+)/$', post_delete, name='delete'),
	url(r'^edit/(?P<id>\d+)/$', post_update, name='update'),
]

if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

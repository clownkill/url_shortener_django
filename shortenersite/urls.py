from django.urls import path, re_path

from .views import index, redirect_original, shorten_url, show_urls

urlpatterns = [
    re_path(r'^$', index, name='home'),
    re_path(r'^(?P<short_id>\w{5})$', redirect_original, name='redirectoriginal'),
    re_path(r'^makeshort/$', shorten_url, name='shortenurl'),
    path('urls/', show_urls, name='showurls')
]

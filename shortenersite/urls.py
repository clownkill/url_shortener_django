from django.urls import path, include

urlpatterns = [
    path('^$', 'index', name='home'),
    path('^(?P<short_id>\w{6})$', 'redirect_original', name='redirectoriginal'),
    path('^makeshort/$', 'shorten_url', name='shortenurl'),
]
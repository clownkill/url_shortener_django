from django.urls import path

from .views import index, redirect_original, shorten_url, show_urls

urlpatterns = [
    path('', index, name='home'),
    path('urls/', show_urls, name='showurls'),
    path('makeshort/', shorten_url, name='shortenurl'),
    path('<slug>/', redirect_original, name='redirectoriginal'),
]

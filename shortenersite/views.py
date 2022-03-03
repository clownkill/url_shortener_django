import random
import hashlib
import string
import json

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings

from .models import Urls

def index(request):
    return render(request, 'shortenersite/index.html')


def show_urls(request):
    context = {
        'urls': Urls.objects.all(),
        'base_url': settings.SITE_URL,
    }
    return render(request, 'shortenersite/urls.html', context)


def redirect_original(request, short_id):
    url = get_object_or_404(Urls, pk=short_id)
    url.count += 1
    url.save()
    return HttpResponseRedirect(url.httpurl)


def shorten_url(request):
    url = request.POST.get('url', '')
    if not (url == ''):
        short_id = get_short_code(url)
        if not(url.startswith('http')):
            url = normalize_url(url)
        b = Urls(httpurl=url, short_id=short_id)
        b.save()

        response_data = {}
        response_data['url'] = settings.SITE_URL + '/' + short_id
        return HttpResponse(json.dumps(response_data), content_type='application/json')
    return HttpResponse(json.dumps({'error': 'error occurs'}), content_type='application/json')

def get_short_code(url):
    while True:
        short_id = hashlib.md5(url.encode()).hexdigest()[:5]
        try:
            temp = Urls.objects.get(pk=short_id)
        except:
            return short_id


def normalize_url(url):
    if url.startswith('www'):
        url = f'http://{url}'
    else:
        url = f'http://www.{url}'
    return url

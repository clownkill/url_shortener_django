from uuid import uuid4

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponseRedirect
from django.conf import settings

from .models import Url



def index(request):
    return render(request, 'shortenersite/index.html')


def show_urls(request):
    context = {
        'urls': Url.objects.all(),
        'base_url': settings.SITE_URL,
    }
    return render(request, 'shortenersite/urls.html', context)


def redirect_original(request, slug):
    url = get_object_or_404(Url, pk=slug)
    url.count_clicks += 1
    url.save()
    return HttpResponseRedirect(url.full_url)


def shorten_url(request):
    url = request.POST.get('url', '')
    if not (url == ''):
        slug = get_short_code()
        if not(url.startswith('http')):
            url = normalize_url(url)
        processed_url = Url(full_url=url, slug=slug)
        processed_url.save()

        response_data = {
            'url': f'{settings.SITE_URL}/{slug}',
        }

        return JsonResponse(response_data)
    return JsonResponse({'error': 'error occurs'})


def get_short_code():
    slug = str(uuid4())[:5]
    return slug


def normalize_url(url):
    if url.startswith('www'):
        url = f'http://{url}'
    else:
        url = f'http://www.{url}'
    return url

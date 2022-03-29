from django.contrib import admin

from shortenersite.models import Url

@admin.register(Url)
class UrlAdmin(admin.ModelAdmin):
    lists_display = ('slug', 'full_url', 'creation_date', 'count_clicks')

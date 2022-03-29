from django.contrib import admin

from shortenersite.models import Urls


class UrlsAdmin(admin.ModelAdmin):
    lists_display = ('slug', 'full_url', 'creation_date', 'count_clicks')


admin.site.register(Urls, UrlsAdmin)

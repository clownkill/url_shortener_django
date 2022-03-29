from django.contrib import admin

from shortenersite.models import Url


class UrlAdmin(admin.ModelAdmin):
    lists_display = ('slug', 'full_url', 'creation_date', 'count_clicks')


admin.site.register(Url, UrlAdmin)

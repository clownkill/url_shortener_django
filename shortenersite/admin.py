from django.contrib import admin

from shortenersite.models import Urls


class UrlsAdmin(admin.ModelAdmin):
    lists_display = ('slug', 'httpurl', 'pub_date', 'count')


admin.site.register(Urls, UrlsAdmin)

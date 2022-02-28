from django.contrib import admin
from django.contrib.auth.models import Group

from refeedit import settings
from refeeds.feed_parser import parse_feed
from refeeds.models import Feed, Entry


class FeedAdmin(admin.ModelAdmin):
    def update(modeladmin, request, queryset):
        for feed in queryset:
            parse_feed(feed)

    list_display = ('name', 'url', 'slug', 'last_scrape',)
    fields = ['name', 'url', 'slug', 'description']
    actions = [update, ]


admin.site.unregister(Group)
admin.site.register(Feed, FeedAdmin)
if settings.DEBUG:
    admin.site.register(Entry)

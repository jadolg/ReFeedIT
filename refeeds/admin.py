from django.contrib import admin
from django.contrib.auth.models import Group
from django.utils.safestring import mark_safe

from refeedit import settings
from refeeds.feed_parser import parse_feed
from refeeds.models import Feed, Entry


class FeedAdmin(admin.ModelAdmin):
    def update(modeladmin, request, queryset):
        for feed in queryset:
            parse_feed(feed)

    @mark_safe
    def refeed_url(self, obj):
        return f"<a href=https://{settings.SITE_DOMAIN}/f/{obj.slug}>/f/{obj.slug}</a>"

    refeed_url.allow_tags = True

    list_display = ('name', 'url', 'refeed_url', 'last_scrape',)
    fields = ['name', 'url', 'slug', 'description']
    actions = [update, ]


admin.site.unregister(Group)
admin.site.register(Feed, FeedAdmin)
if settings.DEBUG:
    admin.site.register(Entry)

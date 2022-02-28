from django.contrib.syndication.views import Feed

from refeeds.models import Feed as ModelFeed, Entry


class FeedView(Feed):
    def get_object(self, request, slug):
        return ModelFeed.objects.get(slug=slug)

    def title(self, obj):
        return obj.name

    def link(self, obj):
        return obj.url

    def description(self, obj):
        return obj.description

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

    def items(self, obj):
        return Entry.objects.filter(feed=obj).order_by('-date_added')[:30]

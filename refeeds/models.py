import hashlib

from django.db import models
from django.db.models import signals
from django.dispatch import receiver
from django.utils.text import slugify


class Feed(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=250, blank=True)
    url = models.URLField()
    last_scrape = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


@receiver(signals.pre_save, sender=Feed)
def populate_slug(sender, instance, **kwargs):
    if instance.slug == "":
        instance.slug = slugify(instance.name)


class Entry(models.Model):
    feed = models.ForeignKey('Feed', on_delete=models.CASCADE)
    title = models.TextField()
    description = models.TextField()
    link = models.URLField()
    hash = models.CharField(max_length=64, unique=True, default=None)
    date_added = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return self.link

    def __str__(self):
        return f"[{self.feed.name}] {self.title}"


def get_entry_hash(title, description, link):
    return f'{hashlib.sha256(f"{title}{description}{link}".encode("utf-8")).hexdigest()}'

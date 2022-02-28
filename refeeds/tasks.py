import logging

from django.utils.timezone import now

from refeedit.celery import app
from refeeds.feed_parser import parse_feed
from refeeds.models import Feed


@app.task(bind=True)
def update_feed_entries(self):
    for feed in Feed.objects.all():
        try:
            parse_feed(feed)
            feed.last_scrape = now()
            feed.save()
        except:
            logging.error(f"ERROR while parsing feed {feed.name}")

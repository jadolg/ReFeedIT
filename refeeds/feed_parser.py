import logging

import feedparser

from refeeds.models import Feed, Entry, get_entry_hash


def parse_feed(feed: Feed):
    feed_reader = feedparser.parse(feed.url)
    for entry in feed_reader.get('entries'):
        if not Entry.objects.filter(hash=get_entry_hash(entry.title, entry.description, entry.link)):
            logging.info(f"saving entry {entry}")
            new_entry = Entry(
                feed=feed,
                title=entry.title,
                description=entry.description,
                link=entry.link,
                hash=get_entry_hash(entry.title, entry.description, entry.link)
            )
            new_entry.save()
        else:
            logging.info(f"entry {entry} already persisted")

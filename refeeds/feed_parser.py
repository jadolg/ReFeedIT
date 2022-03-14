import logging

import feedparser

from refeeds.models import Feed, Entry, get_entry_hash


def parse_feed(feed: Feed):
    feed_reader = feedparser.parse(feed.url)
    for entry in feed_reader.get('entries'):
        entry_hash = get_entry_hash(entry.get("title", "???"),
                                    entry.get("description", "???"),
                                    entry.get("link", "???"))
        if not Entry.objects.filter(hash=entry_hash):
            logging.debug(f"saving entry {entry}")
            new_entry = Entry(
                feed=feed,
                title=entry.get("title", "???"),
                description=entry.get("description", "???"),
                link=entry.get("link", "???"),
                hash=entry_hash
            )
            new_entry.save()
        else:
            logging.debug(f"entry {entry} already persisted")

import hashlib
import logging
from argparse import ArgumentParser
from dateutil import parser

import feedparser
from django.core.exceptions import ValidationError
from django.core.management import BaseCommand, CommandError

from app.spider.models import Newsfeed, Newsitem

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Crawl one or all newsfeeds."

    def add_arguments(self, parser: ArgumentParser):
        parser.add_argument('--one', type=str,
                            help='Fetch news from this one newsfeed, by ID.')
        parser.add_argument('--all', action='store_const', const=True,
                            help="Fetch news from all registered newsfeeds.")

    def handle(self, *args, **options):
        if options.get('all') is True and options.get('one') is not None:
            raise CommandError("Can't have both --all and --one.")

        if options.get('one'):
            self._process_one(options.get('one'))
        elif options.get('all'):
            self._process_all()
        else:
            raise CommandError("Enter either --all or --one.")

    def _process_one(self, id):
        try:
            self._process_feed(Newsfeed.objects.filter(id=id).get())
        except ValidationError as e:
            for message in e.messages:
                self.stderr.write(message)
            raise CommandError("Invalid input.")

    def _process_all(self):
        for feed in Newsfeed.objects.filter(active=True):
            self._process_feed(feed)

    def _process_feed(self, newsfeed: Newsfeed):
        self.stdout.write("Fetch %s" % newsfeed.description)
        feed_content = feedparser.parse(newsfeed.url)
        for entry in feed_content['entries']:
            try:
                id = hashlib.sha1(str(entry.get('id') or entry['link']).encode()).hexdigest()
                if Newsitem.objects.filter(id=id).count() > 0:
                    continue
                Newsitem.objects.create(title=entry['title'],
                                        url=entry['link'],
                                        id=id,
                                        published=parser.parse(entry['published']),
                                        newsfeed=newsfeed) \
                    .save()
            except Exception as e:
                logger.error(str(e))

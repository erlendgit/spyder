from argparse import ArgumentParser

from django.core.management import BaseCommand, CommandError

from app.spider.models import Newsfeed


class Command(BaseCommand):
    help = "Crawl one or all newsfeeds."

    def add_arguments(self, parser: ArgumentParser):
        parser.add_argument('--one', type=str,
                            help='Fetch news from this one newsfeed, by ID.')
        parser.add_argument('--all', action='store_const', const=True,
                            help="Fetch news from all registered newsfeeds.")

    def handle(self, *args, **options):
        if options.get('all') is True and options.get('one') is not None:
            raise CommandError("Can't have both --all and --one")

        if options.get('one'):
            self._process_feed(options.get('one'))
        else:
            for feed in Newsfeed.objects.all():
                self._process_feed(feed.id)

    def _process_feed(self, id):
        pass

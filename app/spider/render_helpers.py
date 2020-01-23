from django.core.paginator import Paginator

from .models import Newsitem


def get_feeditems_context(current_page, count=15, category=''):
    if category:
        newsitems = Newsitem.objects.filter(newsfeed__category=category)
    else:
        newsitems = Newsitem.objects.all()
    paginator = Paginator(newsitems, count)
    return {
        'items': paginator.get_page(current_page),
        'count': count,
        'category': category,
    }

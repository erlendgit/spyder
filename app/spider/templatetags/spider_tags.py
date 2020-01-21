from django import template

from app.spider.models import Newsitem

register = template.Library()


@register.inclusion_tag('spider/feeditems.html')
def all_feeditems():
    return {
        'items': Newsitem.objects.all()[:15]
    }


@register.inclusion_tag('spider/feeditems.html')
def fast_feeditems():
    return {
        'items': Newsitem.objects.filter(newsfeed__category='fast')[:30]
    }

@register.inclusion_tag('spider/feeditems.html')
def normal_feeditems():
    return {
        'items': Newsitem.objects.filter(newsfeed__category='normal')[:15]
    }

@register.inclusion_tag('spider/feeditems.html')
def slow_feeditems():
    return {
        'items': Newsitem.objects.filter(newsfeed__category='slow')[:10]
    }

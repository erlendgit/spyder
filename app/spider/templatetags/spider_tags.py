from django import template

from app.spider.render_helpers import get_feeditems_context

register = template.Library()


@register.inclusion_tag('spider/feeditems.html', takes_context=True)
def feeditems(context, count=15, category=''):
    return get_feeditems_context(
        current_page=context.get('request').GET.get('page'),
        count=count,
        category=category
    )

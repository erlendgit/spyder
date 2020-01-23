from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from app.spider.render_helpers import get_feeditems_context


def load_feeditems(request: WSGIRequest):
    return render(request, 'spider/feeditems.html',
                  get_feeditems_context(
                      current_page=request.GET.get('next_page'),
                      count=request.GET.get('count'),
                      category=request.GET.get('category')
                  ))

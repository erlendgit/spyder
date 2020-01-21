from django.conf import settings
from django.core.handlers.wsgi import WSGIRequest
from django.utils import translation


def common_meta_assets(request: WSGIRequest):
    return {
        'SITE_TITLE': settings.SITE_TITLE,
        'LANGUAGE_CODE': translation.get_language(),
    }

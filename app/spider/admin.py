from django.contrib import admin

from .models import Newsfeed, NewsfeedAdmin

admin.site.register(Newsfeed, NewsfeedAdmin)
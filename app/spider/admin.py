from django.contrib import admin

from .models import Newsfeed, NewsfeedAdmin, Feedcategory, FeedcategoryAdmin

admin.site.register(Newsfeed, NewsfeedAdmin)
admin.site.register(Feedcategory, FeedcategoryAdmin)
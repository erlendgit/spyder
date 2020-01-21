import uuid

from django.contrib import admin
from django.db import models


class Newsfeed(models.Model):
    """ Newsfeed, details about a rss feed.
    """

    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    url = models.URLField(null=False)
    description = models.CharField(max_length=255, null=False)
    active = models.BooleanField(default=True)


class NewsfeedAdmin(admin.ModelAdmin):
    fields = ('id', 'description', 'active', 'url')
    list_display = ('description', 'active', 'url')
    readonly_fields = ('id',)


class Newsitem(models.Model):
    """ Newsitem, details about the newsitem.
    """

    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, null=False)
    target = models.URLField(null=False)
    published = models.DateTimeField(null=False)
    newsfeed = models.ForeignKey(to='Newsfeed', on_delete=models.CASCADE)
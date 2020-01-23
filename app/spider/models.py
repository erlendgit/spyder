import uuid

from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple


class Newsfeed(models.Model):
    """ Newsfeed, details about a rss feed.
    """

    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    url = models.URLField(null=False)
    description = models.CharField(max_length=255, null=False)
    active = models.BooleanField(default=True)
    slug = models.CharField(max_length=10, null=True, blank=True)
    category = models.ManyToManyField(to='spider.Feedcategory', related_name='category', blank=True)


class NewsfeedAdmin(admin.ModelAdmin):
    fields = ('id', 'description', 'slug', 'url', 'category', 'active')
    list_display = ('description', 'slug', 'url', 'active')
    readonly_fields = ('id',)

    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple}
    }


class Feedcategory(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    title = models.CharField(max_length=32, null=False)

    class Meta:
        verbose_name = 'Feed category'
        verbose_name_plural = 'Feed categories'

    def __str__(self):
        return self.title


class FeedcategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'id')


class Newsitem(models.Model):
    """ Newsitem, details about the newsitem.
    """
    id = models.TextField(primary_key=True, max_length=40, null=False)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, null=False)
    url = models.URLField(null=False)
    published = models.DateTimeField(null=False)
    newsfeed = models.ForeignKey(to='Newsfeed', on_delete=models.CASCADE)
    tags = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-published']

from __future__ import unicode_literals

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes =  models.IntegerField(default=0)

    def __str__(self):  # For Python 2, use __unicode__ too
        return self.name
    def __unicode__(self):
        return self.title


class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):  # For Python 2, use __unicode__ too
        return self.title
    def __unicode__(self):
        return self.title
from __future__ import unicode_literals
from django.db import models


class Host(models.Model):
    ip_address = models.CharField(max_length=16)
    port = models.IntegerField()
    name = models.CharField(max_length=256)


class TestSuite(models.Model):
    name = models.CharField(max_length=256)
    text = models.TextField()
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.name
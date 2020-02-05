from django.db import models


class Event(models.Model):
    title = models.CharField('Title', max_length=50)
    description = models.TextField('Description')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    active = models.BooleanField()

    def __str__(self):
        return self.title

from django.db import models


class Todo(models.Model):
    title = models.CharField('Title', max_length=50)
    description = models.TextField('Description')
    created = models.DateTimeField(auto_now_add=True)
    due = models.DateTimeField()

    def __str__(self):
        return self.title

from django.db import models
from django.conf import settings


class Season(models.Model):
    name = models.CharField(max_length=75, default=None)
    league = models.ForeignKey('League', on_delete=models.CASCADE,)

    def __str__(self):
        return self.name

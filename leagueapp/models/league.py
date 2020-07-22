from django.db import models
from django.conf import settings


class League(models.Model):
    name = models.CharField(max_length=75, default=None)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return self.name

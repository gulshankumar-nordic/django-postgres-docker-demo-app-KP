from django.db import models
from django.conf import settings


class Match(models.Model):
    host = models.ForeignKey(
        'TeamSeason', on_delete=models.PROTECT,
        related_name='+',
    )
    guest = models.ForeignKey(
        'TeamSeason', on_delete=models.PROTECT,
    )
    match_date = models.DateTimeField()
    score = models.CharField(max_length=10, default=None)

    def __str__(self):
        return f'{self.host} {self.guest}'
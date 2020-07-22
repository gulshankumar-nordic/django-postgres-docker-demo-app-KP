from django.db import models
from django.conf import settings


class Player(models.Model):
    first_name = models.CharField(max_length=75, default=None)
    last_name = models.CharField(max_length=75, default=None)
    height = models.FloatField(max_length=25, default=None, help_text='In cms')
    weight = models.FloatField(max_length=25, default=None, help_text='In kgs')
    date_of_birth = models.DateField(max_length=75, default=None)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class PlayerInTeam(models.Model):
    player = models.ForeignKey(
        'Player', on_delete=models.CASCADE,
    )
    team = models.ForeignKey(
        'Team', on_delete=models.CASCADE,
    )

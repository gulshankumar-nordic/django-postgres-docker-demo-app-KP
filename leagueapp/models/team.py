from django.db import models
from django.conf import settings


class Team(models.Model):
    name = models.CharField(max_length=75, default=None)
    location = models.TextField(max_length=75, default=None)

    def __str__(self):
        return self.name


class TeamSeason(models.Model):
    name = models.CharField(max_length=75, default=None)
    season = models.ForeignKey('Season', on_delete=models.CASCADE,)
    team = models.ForeignKey('Team', on_delete=models.CASCADE,)

    def __str__(self):
        return self.name

from django.db import models
from utils.models import TimeStampedModel, UUIDModel

class Team(UUIDModel, TimeStampedModel):
    name = models.CharField(max_length=255, null=False, unique=True)

class Player(UUIDModel, TimeStampedModel):
    email = models.EmailField(unique=True, null=True)
    name = models.CharField(max_length=255, null=False, unique=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

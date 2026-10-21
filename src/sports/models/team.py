from django.db import models

class Team(models.Model):
    abbreviation = models.CharField(max_length=5, null=True)

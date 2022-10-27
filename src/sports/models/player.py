from django.db import models

class Player(models.Model):
    playerLastName = models.CharField(max_length=50)
    playerFirstName = models.CharField(max_length=50, null=True)
    playerSlug = models.CharField(max_length=100)
    jerseyNumber = models.CharField(max_length=10, null=True)
    position = models.CharField(max_length=10, null=True)
    height = models.CharField(max_length=5, null=True)
    weight = models.IntegerField(null=True)
    college = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=50, null=True)
    draftYear = models.IntegerField(null=True)
    draftRound = models.IntegerField(null=True)
    draftNumber = models.IntegerField(null=True)
    rosterStatus = models.IntegerField(null=True)
    fromYear = models.IntegerField()
    toYear = models.IntegerField()
    objects = models.Manager()

    def getFullName(self):
        return self.playerFirstName + ' ' + self.playerLastName

    def __str__(self):
        return self.getFullName()

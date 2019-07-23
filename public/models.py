from django.db import models


class MadLibs(models.Model):
    madlib = models.CharField(max_length=50, unique=True)
    votes = models.IntegerField(default=0)

    def up_vote(self):
        self.votes += 1
        self.save()


class IpAddress(models.Model):
    ip = models.GenericIPAddressField(unique=True)


class WordType(models.Model):
    name = models.CharField(max_length=35, unique=True)
    description = models.CharField(max_length=200)


class GameParameters(models.Model):
    parameter = models.CharField(max_length=15, unique=True)
    parameter_value = models.CharField(max_length=50)
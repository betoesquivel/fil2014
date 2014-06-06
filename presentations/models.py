from django.db import models

# Create your models here.
class Presentator(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class Conference(models.Model):
    name = models.CharField(max_length=100)
    room = models.CharField(max_length=10)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    presentators = models.ManyToManyField(Presentator)

    def __unicode__(self):
        return self.name

class BookPresentation(models.Model):
    name = models.CharField(max_length=100)
    room = models.CharField(max_length=10)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    presentators = models.ManyToManyField(Presentator)

    def __unicode__(self):
        return self.name

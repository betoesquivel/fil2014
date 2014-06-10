from django.db import models
from datetime import datetime

# Create your models here.
# This is just in order to get some extra info on the use for the db
class Search(models.Model):
	query = models.CharField(max_length=100)
	requests = models.IntegerField(default=1)
	author = models.BooleanField(default=False)
	book = models.BooleanField(default=False)
	category = models.BooleanField(default=False)
	searchDateTime = models.DateTimeField(default=datetime.now)

	def __unicode__(self):
		return self.query


from django.db import models

# Create your models here.
class Exhibitor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)

    def __unicode__(self):
        return self.name

class Workshop(models.Model):
    name = models.CharField(max_length=50)
    ages = models.CharField(max_length=15, default='Todas')

    def __unicode__(self):
        return self.name

class WorkshopEvents(models.Model):
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    eventDescription = models.CharField(max_length=500)
    workshop = models.ForeignKey(Workshop)

    def __unicode__(self):
        start = self.startTime.strftime('%m-%d-%Y %H:%M:%S')
        return u'%s %s' % (self.workshop.name, start)

class Stand(models.Model):
    location = models.CharField(max_length=10)
    exhibitor = models.ForeignKey(Exhibitor)
    workshop = models.ForeignKey(Workshop)

    def __unicode__(self):
        owner = ''
        if self.exhibitor is not None:
            owner = self.exhibitor.name
        else:
            owner = self.workshop.name
        return u'%s %s' % (self.location, owner)

class Editorial(models.Model):
    name = models.CharField(max_length=50)
    exhibitor = models.ForeignKey(Exhibitor)

    def __unicode__(self):
        return u'%s %s' % (self.name, self.exhibitor.name)

class Book(models.Model):
    title = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)
    synopsis = models.CharField(max_length=1500)
    priority = models.IntegerField(default=3)
    editorial = models.ForeignKey(Editorial)

    def __unicode__(self):
        return u'%s %s' % (self.title, self.editorial.name)

class Author(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)

    def __unicode__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)
    book = models.ForeignKey(Book)

    def __unicode__(self):
        return self.name

class Award(models.Model):
    name = models.CharField(max_length=50)
    book = models.ForeignKey(Book)
    author = models.ForeignKey(Author)

    def __unicode__(self):
        return self.name

class Volunteer(models.Model):
    name = models.CharField(max_length=50)
    studentID = models.CharField(max_length=9)

    def __unicode__(self):
        return self.name

class BookRegistered(models.Model):
    volunteer = models.ForeignKey(Volunteer)
    book = models.ForeignKey(Book)

    def __unicode__(self):
        return u'%s %s' % (self.volunteer.name, self.book.name)





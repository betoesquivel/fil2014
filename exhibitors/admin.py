from django.contrib import admin
from exhibitors.models import Exhibitor, Workshop, WorkshopEvents, Stand, Editorial, Book, Author, Category, Award, Volunteer, BookRegistered

# Register your models here.
admin.site.register(Exhibitor)
admin.site.register(Workshop)
admin.site.register(WorkshopEvents)
admin.site.register(Stand)
admin.site.register(Editorial)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Award)
admin.site.register(Volunteer)
admin.site.register(BookRegistered)

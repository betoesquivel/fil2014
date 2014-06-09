from django.contrib import admin
from presentations.models import Presentator, Conference, BookPresentation

# Register your models here.
admin.site.register(Presentator)
admin.site.register(Conference)
admin.site.register(BookPresentation)

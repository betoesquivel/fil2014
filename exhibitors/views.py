from django.shortcuts import render, render_to_response
from exhibitors.models import Book, Author, Exhibitor

# Create your views here.
def books(request):
    return render_to_response('baseSearch.html', {'activeTab':"libros"})

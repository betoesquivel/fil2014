from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from exhibitors.models import Book, Author, Exhibitor
import json

# Create your views here.
def books(request):
    return render_to_response('books.html', {'activeTab':"libros"})

def getBooks(request):
    q = request.GET.get('query', '')
    data_to_dump = {
        'query' : q,
    }
    data = json.dumps(data_to_dump)
    return HttpResponse(data, content_type='application/json')

def workshops(request):
    return render_to_response('baseSearch.html', {'activeTab':"talleres"})

# for all the exhibitors at the fair with no books and other products instead
def others(request):
    return render_to_response('baseSearch.html', {'activeTab':"otros"})

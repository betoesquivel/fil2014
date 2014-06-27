from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from exhibitors.models import Book, Author, Exhibitor
from functions import generalGoogleQuery
from forms import BooksSearchForm
import json

# Create your views here.
def books(request):
    return render_to_response('books.html', {'activeTab':"libros"})

def getBooks(request):
    print "Baby steps"
    # we retrieve the query to display it in the template
    form = BooksSearchForm(request.GET)
    print "Created the form object"

    # we call the search method from the Bookssearchform. Haystack do the work!
    haystackResults = form.search()
    print "Made the search"

    print "No errors on db search..."
    for sr in haystackResults:
        print sr.object.title
        print sr.object.author_set.all()
        print sr.object.editorial.name
        print sr.object.editorial.exhibitor.name
        print sr.object.editorial.exhibitor.stand_set.all()

    q = request.GET.get('q', '')
    print "Query..."
    print q
    data_to_dump = generalGoogleQuery(q)
    data = json.dumps(data_to_dump)
    return HttpResponse(data, content_type='application/json')

def workshops(request):
    return render_to_response('baseSearch.html', {'activeTab':"talleres"})

# for all the exhibitors at the fair with no books and other products instead
def others(request):
    return render_to_response('baseSearch.html', {'activeTab':"otros"})

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
    dbResults = {'results':[], 'totalItems':len(haystackResults)}
    for sr in haystackResults:
        b = sr.object
        title = b.title
        authors = b.author_set.all()
        editorial = b.editorial.name
        exhibitor = b.editorial.exhibitor.name
        stands = b.editorial.exhibitor.stand_set.all()
        newResult = {
            'title': title,
            'authors': [],
            'editorial': editorial,
            'exhibitor': exhibitor,
            'stands': [],
        }
        for a in authors:
            newResult['authors'].append(a.name)
        for s in stands:
            newResult['stands'].append(s.location)
        dbResults['results'].append(newResult)

    print json.dumps(dbResults, indent=4)

    q = request.GET.get('q', '')
    print "Query..."
    print q
    data_to_dump = generalGoogleQuery(q)
    data_to_dump['dbResults'] = dbResults
    data = json.dumps(data_to_dump)
    return HttpResponse(data, content_type='application/json')

def workshops(request):
    return render_to_response('baseSearch.html', {'activeTab':"talleres"})

# for all the exhibitors at the fair with no books and other products instead
def others(request):
    return render_to_response('baseSearch.html', {'activeTab':"otros"})

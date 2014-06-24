import urllib
import json
from exhibitors.models import Book, Author, Exhibitor, Editorial, Stand

def findGoogleResultsInDb(isbns):
    ourDbResults = {}
    results = []
    # query db and get all the isbns
    isbnsQuery = Book.objects.all().values('isbn')
    # extract results from my list of dicts into a list of strings
    dbIsbns = []
    for isbnItem in isbnsQuery:
        dbIsbns.append(isbnItem['isbn'])

    # cycle the received isbns gotten from the google search
    for googleIsbn in isbns:
        if googleIsbn in dbIsbns:
            # query db and get the book with that isbn
            b = Book.objects.filter(isbn=googleIsbn)[0]

            # extract only the useful information and
            # build the dict result
            result = {
                'title': b.title,
                'author': [],
                'editorial': b.editorial.name,
                'exhibitor': b.editorial.exhibitor.name,
                'stands': [],
            }
            authors = b.author_set.all()
            for a in authors:
                result['author'].append(a.name)

            stands = b.editorial.exhibitor.stand_set.all()
            for s in stands:
                result['stands'].append(s.location)

            # add the result to our results list
            results.append(result)

    ourDbResults['totalItems'] = len(results)
    ourDbResults['results'] = results
    return ourDbResults

# queries the db and gets the stands of that exhibitor
def findPossibleStands(exhibitor):
    stands = exhibitor.stand_set.all()
    return stands

# queries the db and gets the exhibitor that has that editorial
def findPossibleExhibitor(editorial):
    editorials = Editorial.objects.filter(name = editorial)
    if len(editorials) > 0:
        editorial = editorials[0]
        exhibitor = editorial.exhibitor
        return exhibitor
    else:
        return None

def parseIndustryIdentifiers(industryIdentifiers):
    isbn = ""
    # after this loop, isbn is either "", ISBN_10 or ISBN_13
    # most of the time it will be ISBN_13
    for industryId in industryIdentifiers:
        if industryId['type'] == "ISBN_13":
            isbn = industryId['identifier']
            return isbn
        else:
            if industryId['type'] == "ISBN_10":
                isbn = industryId['identifier']
    return isbn

def parseGoogleResults(googleResults):
    ourResults = {}
    ourResults['totalItems'] = googleResults['totalItems']

    items = googleResults['items']
    ourItems = []
    ourIsbns = []
    for item in items:
        # Get important information from the google result item
        # Use it to guess where the item would be in our db
        # add newItem to ourItems that contains the parsed google results
        info = item['volumeInfo']
        if 'industryIdentifiers' in info:
            newItem = {
                'title': '-',
                'author': '-',
                'editorial': '-',
                'exhibitor': '-',
                'stands' : [],
            }
            if 'title' in info:
                newItem['title'] = info['title']
            if 'authors' in info:
                newItem['author'] = info['authors']
            if 'publisher' in info:
                newItem['editorial'] = info['publisher']
                foundExhibitor = findPossibleExhibitor(newItem['editorial'])
                if foundExhibitor is not None:
                    newItem['exhibitor'] = foundExhibitor.name
                    stands = findPossibleStands(foundExhibitor)
                    for s in stands:
                        newItem['stands'].append(s.location)

            ourItems.append(newItem)

            # Get ISBN_13 or, if missing, ISBN_10.
            # And add the isbn to our list
            newIsbn = parseIndustryIdentifiers(info['industryIdentifiers'])
            ourIsbns.append(newIsbn)

    ourResults['results'] = ourItems
    ourResults['isbns'] = ourIsbns
    return ourResults

# Encodes an unadvanced search (no "") with + separating terms
# Makes the request to the google books api
# Returns a python dictionary with the results
def generalGoogleQuery(query):
    url = 'https://www.googleapis.com/books/v1/volumes?q=%s' %query
    searchResponse = urllib.urlopen(url)
    searchResults = searchResponse.read()
    # extract useful information from google results
    googleResults = parseGoogleResults(json.loads(searchResults))
    ourDbResults = findGoogleResultsInDb(googleResults['isbns'])

    results = {
        'dbResults': ourDbResults,
        'googleResults': googleResults,
    }
    print "RESULTS============="
    print json.dumps(results, indent=4)

    return results

def byAuthorGoogleQuery(query):
    encodedQuery = urllib.urlencode({'q':query})
    url = 'https://www.googleapis.com/books/v1/volumes?%s' % encodedQuery
    searchResponse = urllib.urlopen(url)
    searchResults = searchResponse.read()
    return searchResults

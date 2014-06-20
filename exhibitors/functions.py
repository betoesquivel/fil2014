import urllib

# Encodes an unadvanced search (no "") with + separating terms
# Makes the request to the google books api
# Returns a python dictionary with the results
def generalGoogleQuery(query):
    encodedQuery = urllib.urlencode({'q':query})
    url = 'https://www.googleapis.com/books/v1/volumes?%s' % encodedQuery
    searchResponse = urllib.urlopen(url)
    searchResults = searchResponse.read()
    return searchResults

def byAuthorGoogleQuery(query):
    encodedQuery = urllib.urlencode({'q':query})
    url = 'https://www.googleapis.com/books/v1/volumes?%s' % encodedQuery
    searchResponse = urllib.urlopen(url)
    searchResults = searchResponse.read()
    return searchResults

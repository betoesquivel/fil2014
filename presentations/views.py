from django.shortcuts import render, render_to_response

# Create your views here.
def presentations(request):
    return render_to_response('baseSearch.html', {'activeTab':'expositores'})

import random
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Wikis

# Create your views here.


def home(request):
    # getting the wikis we'll deisplay in home page
    wikisToLoop = Wikis.objects.all().order_by('date')
    # rendering the template
    return render(request, 'home.html', {'wikis': wikisToLoop})

def randomWiki(request):
    wikis = Wikis.objects.all()
    #getting the random wiki
    randomWiki = random.choice(wikis)
    #rendring the wiki page with the random wiki we got
    return render(request, "wiki.html", {'wiki': randomWiki})

def add(request):
    #if the user sends the form
    if request.method == 'POST':
    #getting user input
        title = request.POST.get('title')
        description = request.POST.get('description')
        details = request.POST.get('details')
    #checking the user input
        if not title or not description or not details:
            return render(request, "add.html", {'error': "invalid input"})
    #storing the wiki in db and saving it
        wiki = Wikis(title=title, description=description, details=details)
        wiki.save()
    #redirecting the user to home page
        return redirect('home')
    #else if the user tried access the page with get
    return render(request, "add.html")

def wiki(request, wiki):
    #getting the wanted wiki from db by it's title
    wantedWiki = Wikis.objects.filter(title=wiki).first()
    #if the user tried to access a wiki that doesn't exict
    if not wantedWiki:
        return HttpResponse('error 404')
    #rendering the wiki template with the wanted wiki
    return render(request, "wiki.html", {'wiki': wantedWiki})

def search(request):
    #getting what wiki user searched for
    search_input = request.GET.get('searchinput')
    #checking if user input is invalid
    if not search_input:
        return redirect("home")
    #getting what user searched for from db
    search_results = Wikis.objects.filter(title__icontains=search_input)
    #checking if it doesn't exict 
    if not search_results.exists():
        return HttpResponse("No results found")
    #rendring the search template
    return render(request, "search.html", {'wikis': search_results})


#def favicon(request):
#return HttpResponse(status=204)
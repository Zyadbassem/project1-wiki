from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Wikis
# Create your views here.


def home(request):
    wikisToLoop = Wikis.objects.all().order_by('date')
    return render(request, 'home.html', {'wikis': wikisToLoop})

def add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        details = request.POST.get('details')
        if not title or not description or not details:
            return HttpResponse("error1")
        wiki = Wikis()
        wiki.title = title
        wiki.description = description
        wiki.details = details
        wiki.save()
        return redirect('home')
        
    return render(request, "add.html")
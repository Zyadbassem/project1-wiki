from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def helloWorld(request):
    return render(request, 'home.html')

def rooms(request):
    return HttpResponse('How many rooms? ')
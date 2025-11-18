from django.http import HttpResponse
from django.shorcuts import render

def home(request):
    # render http response
   # return HttpResponse('<h1>Home</h1>')
    # render html page
    return render (request, "home.html")
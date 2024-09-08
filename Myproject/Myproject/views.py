# from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # return HttpResponse('hellw there , this is my home page ')
    return render (request, 'home.html')
def about (request):
    # return HttpResponse('  this is my about page ')
    return render (request, 'about.html')
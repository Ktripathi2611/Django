from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    # return HttpResponse("hello u are at the home page")
    return render(request, 'index.html')
def about(request):
    return HttpResponse("hello u are at the about page")
def contact(request):
    return HttpResponse("hello u are at the contact page")
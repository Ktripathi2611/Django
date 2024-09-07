from django.http import HttpResponse

def home(request):
    return HttpResponse("hello u are at the home page")
def about(request):
    return HttpResponse("hello u are at the about page")
def contact(request):
    return HttpResponse("hello u are at the contact page")
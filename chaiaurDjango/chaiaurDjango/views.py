from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello World!! You are at chai aur Django Homepage")
    return render(request, 'website/index.html')

def about(request):
    # return HttpResponse("Hello World!! You are at chai aur Django About Page")
    return render(request, 'website/about.html')
    
def contact(request):
    # return HttpResponse("Hello World!! You are at chai aur Django Contact Page")
    return render(request, 'website/contact.html')
    
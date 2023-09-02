from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def AboutPage(request):
    return render(request, 'about-me.html')

def BlogPage(request):

    return render(request, 'blog-grid.html')

def ContactPage(request):
    return render(request, 'contact-2.html')

def IndexPage(request):
    return render(request, 'index-dark.html')

def ServicePage(request):
    return render(request, 'services.html')

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def about_me(request):
    return render(request, 'about/about-me.html')

# def about_me(request):
#     return HttpResponse ('Here Aviliable lots.')
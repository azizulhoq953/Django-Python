from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def contact(request):
    return render(request, 'contact-2.html')

# def about_me(request):
#     return HttpResponse ('Here Aviliable lots.')
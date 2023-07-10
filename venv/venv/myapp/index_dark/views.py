from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index_dark(request):
    return render(request, 'index/index-dark.html')

# def about_me(request):
#     return HttpResponse ('Here Aviliable lots.')
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def wrap(request):
    return render(request, 'services/wrap.html')

# def about_me(request):
#     return HttpResponse ('Here Aviliable lots.')
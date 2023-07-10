from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def blog_grid(request):
    return render(request, 'blog/blog-grid.html')

# def about_me(request):
#     return HttpResponse ('Here Aviliable lots.')
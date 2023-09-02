from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

#same view is same folder urls

def database(request):
    return render(request, 'main.html')

def main(request):
    teach = main.object.all()
    return render (request, 'main.html', {'thr': teach})
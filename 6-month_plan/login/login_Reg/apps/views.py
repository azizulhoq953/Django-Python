from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def LoginPage(request):
    return render(request, 'login.html')

def RegisterPage(request):

    return render(request, 'register.html')

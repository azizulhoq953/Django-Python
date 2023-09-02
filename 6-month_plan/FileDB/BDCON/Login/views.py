from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext

from Login.forms import UserRegis

# Create your views here.

def Login_p(request):
    return render(request, 'about.html')


def FormData(request):
    # fm =UserRegis()
    if request.method == 'POST':
        fm = UserRegis(request.POST)
        if fm.is_valid():
         print(fm.cleaned_data['password'])
         print(fm.cleaned_data['repassword'])
        # print('This Is Post')

    else:
       fm = UserRegis()
       print('This Is GET')
    
    return render (request, 'login.html',{'form':fm})
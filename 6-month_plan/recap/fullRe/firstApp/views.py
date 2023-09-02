from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext

from .forms import UserRegis



def login(request):
    if request.method == 'POST':
        fm = UserRegis(request.POST)
        if fm.is_valid():
            print(fm.cleaned_data['password'])
            print(fm.cleaned_data['repassword'])
    else:
        fm = UserRegis()
        print('This is Gate')

    return render(request, 'login.html',{'form':fm})
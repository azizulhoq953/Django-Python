from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext
from about.forms import StudentsReg
def about_us(request):
    return render(request, 'about/mission.html')


def showformsdata(request):
    if request.method == 'POST':
     fm = StudentsReg(request.POST)
     if fm.is_valid():
        print(fm.cleaned_data['password'])
        print(fm.cleaned_data['repassword'])
    else:
       fm = StudentsReg()
       print('This Is GET')
    
    return render(request,'form.html',{'form':fm})
from django.http import HttpResponse
from django.shortcuts import render
from database.forms import TeachersRegistration

# Create your views here.

#same view is same folder urls

def databaseV(request):
    return render(request, 'index.html')



def showformsdata(request):
     fm = TeachersRegistration()
     fm.order_fields(field_order=['email','last_name','firs_name'])
     return render(request, 'blogs/form.html', {'form':fm})

# def teachers_info(request):
#     teach = teacher.object.all()
#     return render (request, 'main.html')
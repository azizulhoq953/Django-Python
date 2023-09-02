from django.shortcuts import render,redirect

from .models import portfolio

def portfolioReq(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        message= request.POST.get("message")

     
        data = portfolio(username=username, email=email, message=message )
        data.save()
    return render(request,'index-11.html',{})



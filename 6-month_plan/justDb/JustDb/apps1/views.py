from django.shortcuts import render
# Create your views here.
# from django.contrib.auth import apps1
from .models import login




# Create your views here.




def loginRe(request):
    if request.method == "POST":
        uname = request.POST.get("uname")
        psw = request.POST.get("psw")
        remember = request.POST.get("remember")
        # phone = request.POST.get['phone']
        # subject= request.POST.get['subject']
        # message= request.POST.get['message']

     
        data = login(uname=uname, psw=psw, remember=remember)
        data.save()
        # return redirect('sucess')

    return render(request,'login.html',{})

# def LoginPage(request):

#     return render(request, 'login.html')


# def success(request):

#     return render(request, 'sucess.html')



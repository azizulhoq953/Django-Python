# from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import authenticate


def signup(request):

    if request.method == "POST":
        username = request.POST.get("username")
      
        password1= request.POST.get("password1")

     
        data = authenticate(username=username, password1=password1 )
        data.save()
    # return redirect('blog.html')

    return render(request,'signup.html',{})









    # if request.method == 'POST':
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         username = form.cleaned_data.get('username')
    #         password = form.cleaned_data.get('password1')
    #         user = authenticate(username=username, password=password)
    #         login(request, user)
    #         return redirect('home')
    # else:
    #     form = UserCreationForm()
    # return render(request, 'signup.html', {'form': form})

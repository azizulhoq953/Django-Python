from django.shortcuts import render,redirect
from .models import shopAdmin,login,authenticate
from django.urls import reverse
from .forms import SignUpForm
from django.contrib.auth.forms import UserCreationForm


def signup(request):

    if request.method == "POST":
        Username = request.POST.get("Username")
        Email= request.POST.get("Email")
        PhoneNumber= request.POST.get("PhoneNumber")
        Password= request.POST.get("Password")
        Password1 = request.POST.get("Password1")
        Location= request.POST.get("Location")

     
        data = authenticate(Username=Username, Password=Password,Password1=Password1,Email=Email,PhoneNumber=PhoneNumber,Location=Location )
        data.save()
        return redirect(reverse('shop'))

    return render(request,'signup.html',{})

# Create your views here.

# def mainPage(request):
    # if request.method == "POST":
    #     username = request.POST.get("username")
    #     email = request.POST.get("email")
    #     phone = request.POST.get("phone")
    #     subject= request.POST.get("subject")
    #     message= request.POST.get("message")

     
        # data = login(username=username, email=email, phone=phone, subject=subject, message=message )
        # data.save()
    # return redirect('blog.html')

    # return render(request,'shop.html',{})

def MainPage(request):
    first_shop = shopAdmin.objects.first()
    three_shop= shopAdmin.objects.all()[1:12]
    #  = shopAdmin.objects.all()[1:12]
    # first_news.id = get_object_or_404(blogAdmin, first_news.id)

    return render(request, 'shop.html',{
        'first_shop ':first_shop ,
        'three_shop':three_shop,
        # 'first_newsid':first_newsid,
    })

# from django.views.decorators.csrf import csrf_exempt
# @csrf_exempt

# def RegsDetails( request):
#     if request.method == 'POST':
#         Username = request.POST.get('Username')
#         Password = request.POST.get('Password')
#         Email = request.POST.get('Email')
#         PhoneNumber = request.POST.get('PhoneNumber')
#         Location= request.POST.get('Location')
      

     
#         data = registration(Username=Username, Password=Password , Email=Email, PhoneNumber=PhoneNumber, Location=Location)
#         data.save()
#         print(data)
#         # return HttpResponse("User Has been Created")

#         # return redirect('login')

#     return render(request,'register.html',{'data':data})






# from django.views.decorators.csrf import csrf_exempt
# @csrf_exempt
# def loginDetails(request):
#     if request.method == 'POST':
#         email=request.POST.get('email')
#         password=request.POST.get('password')


#         form = login(email=email, password=password)
#         form.save()

#         # return redirect('/profile')
#     return render (render, 'login.html',{'form': form})




def productDetail(request):

    return render(request,"product-details.html",{})


def cartDetail(request):


    return render(request,"cart.html",{})

def checkOut (request):
    

    return render(request,"checkout.html",{})


def priceDetails(request):

    return render(request,'pricing.html',{})


def loginDetails(request):


 if request.method == "POST":
        email = request.POST.get("email")
        password= request.POST.get("password")
       

     
        data = login(email=email, password=password )
        data.save()
    # return redirect('blog.html')

        return redirect(reverse('shop'))

 return render(request,'login.html',{})


def RegsDetails(request):

    return render(request,'register.html',{})

def profileDetails(request):

    return render(request,'profile.html',{})
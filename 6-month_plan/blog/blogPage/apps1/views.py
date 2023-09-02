from django.shortcuts import render,redirect,get_object_or_404

# from django.contrib.auth import apps1
from .models import login,blogAdmin



# Create your views here.


# def LoginPage(request):

#     return render(request, 'login.html')

def loginReq(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        subject= request.POST.get("subject")
        message= request.POST.get("message")

     
        data = login(username=username, email=email, phone=phone, subject=subject, message=message )
        data.save()
    # return redirect('blog.html')

    return render(request,'contact.html',{})


def AddMoreView(request):
    return render(request, 'details.html')

def MainPage(request):
    first_news = blogAdmin.objects.first()
    three_news = blogAdmin.objects.all()[1:12]
    first_newsid = blogAdmin.objects.all()[1:12]
    # first_news.id = get_object_or_404(blogAdmin, first_news.id)

    return render(request, 'blog.html',{
        'first_news':first_news,
        'three_news':three_news,
        # 'first_newsid':first_newsid,
    })


def ContactPage(request):
    return render(request, 'contact.html')








# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST.get['username']
#         email = request.POST.get['email']
#         phone = request.POST.get['phone']
#         subject= request.POST.get['subject']
#         message= request.POST.get['message']

     
#         data = login.object.create_user(username=username,email=email,phone=phone,subject=subject,message=message)
#         data.save()
#         return redirect('blog')

#     return render(request,'contact.html')


# def MainPage(request):
#     return render(request, 'blog.html')



# def user_login(request):
#     if request.method == 'POST':
#         Usearname = request.POST.get['Usearname']
#         Password = request.POST.get['Password']
  
     
#         data = singup.create_newObj.authenticate(Usearname=Usearname,Password=Password)
#         data.save()
#         return redirect('blog')

#     return render(request,'contact.html')




    #         if user is not None:
    #             return render(request,'blog.html', {})
    #         else:
    #             print("Someone tried to login and Faild")
    #             print("They used Name: {} and Password:{}".format(username=username,email=email,phone=phone,subject=subject,message=message))

    #             return redirect('/')
    #     except Exception as identifier:
    #         return redirect('/')
        
    # else:
    #     return render(request,'contact.html')
from django.contrib import admin
from apps1.models import login
from apps1.models import blogAdmin

class userlogin(admin.ModelAdmin):
    list_display = ('username','email','phone','subject','message',)
    search_fields= ('phone',)
    list_filter =('username',)

class userBlogAdmin(admin.ModelAdmin):
    list_display = ('title','description','image','date',)
    search_fields= ('title',)
    list_filter =('title',)
   
# Register your models here.
admin.site.register(login,userlogin)
admin.site.register(blogAdmin,userBlogAdmin)

from django.contrib import admin
from mainApp.models import portfolio

# Register your models here.
class userPort(admin.ModelAdmin):
    list_display = ('username','email','message',)
    search_fields= ('username',)
    ist_filter =('email',)


admin.site.register(portfolio,userPort)

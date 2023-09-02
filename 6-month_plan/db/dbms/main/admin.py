from django.contrib import admin
from main.models import main
from database.models import Student_info

# Register your models here.
# class mainAdmin(admin.ModelAdmin):
#     list_display = ('main_ID','main_Name','main_Email')

admin.site.register(main)
admin.site.register(Student_info)
# admin.site.register(mainAdmin)
 

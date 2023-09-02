from django.contrib import admin
from about.models import teacher
# from . models import contactEnquiries

# class ContactAdmin(admin.ModelAdmin):
#     list_display =  ['cn_name', 'cn_email', 'cn_number']

   
#     def cn_name(self, obj):
#         return obj.cn_name
    
#     cn_name.short_description = 'Name'

#     def cn_email(self, obj):
#         return obj.cn_email
    
#     cn_email.short_description = 'Email'


# admin.site.register(contactEnquiries, ContactAdmin)

admin.site.register(teacher)



# class teacher(models.Model):
#     Tid = models.IntegerField()
#     TName = models.CharField()
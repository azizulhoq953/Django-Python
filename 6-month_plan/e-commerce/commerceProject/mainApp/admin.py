from django.contrib import admin
from mainApp.models import shopAdmin,authenticate,login,defaultd

# Register your models here.
# admin.site.register(cartdb)
# class cartdb(admin.ModelAdmin):
#     list_display =  ['Item', 'Price', 'Quantity','Total']
#     def Item(self, obj):
#         return obj.Item
    
#     Item.short_description = 'Name'

#     def Price(self, obj):
#         return obj.Price
    
#     Price.short_description = 'Price'

#     def Quantity(self, obj):
#         return obj.Quantity
    
#     Quantity.short_description = 'Quantity'

#     def Total(self, obj):
#         return obj.Quantity
    
#     Total.short_description = 'Total'



# admin.site.register(Deleted)
admin.site.register(shopAdmin)
admin.site.register(authenticate)
admin.site.register(login)
admin.site.register(defaultd)

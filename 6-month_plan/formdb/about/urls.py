from django.urls import path
from . import views


urlpatterns = [
    path('a/',views.about_us),
    path('f/',views.showformsdata), #it's call fuctionName
    
]
from django.urls import path
from . import views

urlpatterns = [
    path('d/',views.databaseV),
    path('f/',views.showformsdata),
    
    # path('blog/',include('blog-grid.urls')),
    # path('contact/',include('contact-2.urls')),
    # path('index/',include('index-dark.urls')),
]
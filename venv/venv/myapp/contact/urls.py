from django.urls import path
from . import views

urlpatterns = [
    path('',views.contact),
    
    # path('blog/',include('blog-grid.urls')),
    # path('contact/',include('contact-2.urls')),
    # path('index/',include('index-dark.urls')),
]

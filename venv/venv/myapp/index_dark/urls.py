from django.urls import path
from . import views

urlpatterns = [
    path('',views.index_dark),
    
    # path('blog/',include('blog-grid.urls')),
    # path('contact/',include('contact-2.urls')),
    # path('index/',include('index-dark.urls')),
]

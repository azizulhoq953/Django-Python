from django.urls import path
from . import views,include
from django.conf.urls import url
from django.contrib.auth.views import(
    service, blog, index, about
)
urlpatterns = [
    path(r'^$',views.about_me),
    path(r'^blog/$',blog, {'teplate_name': 'blog-grid.html'}),
    path(r'^service/$',service, {'template_name': 'services.html'}),
    path(r'^index/$',index, {'template_name': 'index-dark.html'}),
    
    # path('blog/',include('AboutPage.urls')),
    # path('contact/',include('BlogPage.urls')),
    # path('index/',include('index-dark.urls')),
]

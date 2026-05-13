from django.contrib import admin
from django.urls import path
from website.views import index_view , about_view , contact_view
app_name = 'website'
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('' , index_view , name='index') ,
    path('about' , about_view , name='about') , 
    path('contact' , contact_view , name='contact') , 
    path('test' , test_view , name='test')
]

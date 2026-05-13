from django.contrib import admin
from django.urls import path
from blog.views import  * 
app_name = 'blog'
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('' , blog_view , name='index') ,
    path('blog/single' , blog_single , name='single') ,

]

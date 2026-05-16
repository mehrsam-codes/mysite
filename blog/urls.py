from django.contrib import admin
from django.urls import path
from blog.views import  * 
app_name = 'blog'
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('' , blog_view , name='index') ,
    path('<int:pid>' , blog_single , name='single') ,
    # path('post-<int:pid>' , test )

]

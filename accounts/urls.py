from django.urls import path
from .views import * 
app_name = 'accounts'
urlpatterns = [
    path('accounts/login/', login_view, name='login'),
    #login
    path('logout' , logout_view , name='logout') , 
    #log out
    path('signup' , signup_view , name='signup') , 
    #signup
]
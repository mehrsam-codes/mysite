from django.shortcuts import render
from django.contrib.auth import authenticate , login , logout 
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm ,UserCreationForm
from django.urls import reverse
from django.contrib import messages
# Create your views here.
def login_view(request):
    if not request.user.is_authenticated:
        if request.method =='POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request , username=username , password= password)
            if user is not None:
                login(request , user)
                return redirect('/')
        form = AuthenticationForm()
        context = {'form':form}
        return render(request , 'accounts/login.html' , context)
    else:
        return redirect('/')
    
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return    redirect('/')

def signup_view(request):
    if not request.user.is_authenticated:

        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'حسابت با موفقیت ساخته شد! حالا می‌تونی وارد بشی.')
                return redirect('/')
        else:
            form = UserCreationForm()
        
        context = {'form': form}
        return render(request, 'accounts/signup.html', context)
    else:
        return redirect('/')
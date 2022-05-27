from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exist")
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "email already exist")
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name= firstname, last_name = lastname, username=username, email=email, password=password)
                    user.save()
                    return redirect('login')
            
        else:
            return redirect('register')
        
    return render(request, 'register.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            return redirect('login')
            
            
    return render(request, 'login.html')


def profile(request):
    return render(request, 'profile.html')

def signout(request):
    logout(request)
    return redirect('profile')
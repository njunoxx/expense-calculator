from django.shortcuts import render, redirect
from django.views import View
from django.contrib import auth
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib import messages



# Create your views here.
class LoginView(View):
    def get(self, request):
        return render(request, 'authentication/login.html')
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, "Successfully Logged in!")
            return redirect('index')
        else:
            messages.error(request, "Username or Password doesnot match!! ")
            return redirect('login')
        
class LogoutView(View):
    def get(self, request):
        user = request
        logout(user)
        messages.success(request, "Logged Out Successfully!")
        return redirect('login')
    
class RegisterView(View):
    def get(self, request):
        return render(request, 'authentication/register.html')

    def post(self, request):
        user = User()
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.save()
        messages.success(request, "User created successfully!")
        return redirect('exp-index')
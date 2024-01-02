from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password,make_password
from django.contrib.auth import login,logout

from django.http import HttpResponse

# Create your views here.
class AuthView:
    @staticmethod
    def register(request):
        if request.method == "POST":
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            if not username or not email or not password:
                return HttpResponse('all fields are mendatory')
            if User.objects.filter(username=username).exists() or User.objects.filter(email=email):
                return HttpResponse('email or username already taken')
            user = User(username=username,email=email,password=make_password(password))
            user.save() 
            return redirect('login')

        return render(request,"register.html")
    
    @staticmethod
    def login(request):
        if request.method == "POST":
            email = request.POST.get('email')
            password = request.POST.get('password')
            if  not email or not password:
                    return HttpResponse('all fields are mendatory')
            user = User.objects.filter(email=email).first()
            if user is not None and check_password(password,user.password):
                login(request,user)
                return redirect('index')
            else:
                return HttpResponse("Invalid login credentials")

        
          
        return render(request,"login.html")
    @staticmethod
    def logout(request):
        logout(request)
        return redirect('index')

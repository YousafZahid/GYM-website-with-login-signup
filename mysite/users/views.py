from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


# Create your views here.

def home(request):
    return render(request, "home.html")

def signup(request):
    if request.method == "GET":
        return render(request, "signup.html")
    elif request.method == "POST":
        user = User.objects.create(first_name=request.POST.get('first_name'), username=request.POST.get('email'), email=request.POST.get('email'))
        user.set_password(request.POST.get('password'))
        user.save()
        return render(request, "loggedin_Home.html")
                        

def login_page(request):
    if request.method == "GET":
        return render(request, "login_page.html")
    elif request.method == "POST":
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:  
            login(request, user)
            return redirect('loggedin_Home')  # Update this to the actual URL name
        else:
            return render(request, 'login_page.html', {'error_message': 'Invalid credentials'})

def loggedin_Home(request):
        return render(request, "loggedin_Home.html")
   
        
        
   





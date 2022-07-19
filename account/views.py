from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    return render(request, 'account/login.html')

def logout(request):
    return redirect('home')

def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname'] #this data comes from register.html form where name='firstname'
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return redirect('register')
        
            else: 
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists')
                    return redirect('register')

                else:
                    user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username, email=email, password=password)
                    auth.login(request, user) #this block of code makes user login automatically
                    messages.success(request, "You are now logged in!")
                    return redirect('dashboard')
                 
                    user.save() #this block of code save user data
                    messages.success(request, "User registered successfully")
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do no match')
            return redirect('register')
            
    else:
        return render(request, 'account/register.html')

def dashboard(request):
    return render(request, 'account/dashboard.html')
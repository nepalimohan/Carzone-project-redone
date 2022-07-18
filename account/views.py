from django.shortcuts import render, redirect

# Create your views here.
def login(request):
    return render(request, 'account/login.html')

def logout(request):
    return redirect('home')

def register(request):
    if request.method == 'POST':
        print("demo")
    return render(request, 'account/register.html')

def dashboard(request):
    return render(request, 'account/dashboard.html')
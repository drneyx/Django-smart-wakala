from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'wakala/auth/login.html')

def login(request):
    return render(request, 'wakala/auth/login.html')

def registration(request):
    return render(request, 'wakala/auth/registration.html')
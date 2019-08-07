from django.shortcuts import render

# Create your views here.


def signup(request):
    return render(request, 'signup.html')

def signup_mento(request):
    return render(request, 'signup_mento.html')

def signup_menti(request):
    return render(request, 'signup_menti.html')

def login(request):
    return render(request, 'login.html')
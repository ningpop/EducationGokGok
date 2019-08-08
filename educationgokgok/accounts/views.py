from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
# 멘토 멘티를 따로 데이터를 저장해줘야할꺼같은데.... 그 부분을 아직 못함....

def signup(request):
    return render(request, 'signup.html')

def signup_mento(request):
    '''
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                request.POST['username'], password=request.POST['password1'], email=request.POST['email'])
            user.profile.phoneNumber = request.POST['phoneNumber']
            user.profile.gender = request.POST['gender']
            auth.login(request, user)
            return redirect('index')
    '''
    return render(request, 'signup_mento.html')

def signup_menti(request):
    '''
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                request.POST['username'], password=request.POST['password1'], email=request.POST['email'])
            user.profile.phoneNumber = request.POST['phoneNumber']
            user.profile.gender = request.POST['gender']
            auth.login(request, user)
            return redirect('index')
    '''
    return render(request, 'signup_menti.html')

def login(request):
    '''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
        return redirect('index')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        eturn render(request, 'login.html')
    '''
'''
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('index')
    return render(request, 'signup.html')
'''
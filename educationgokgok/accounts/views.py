from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from .forms import UserForm , ProfileForm
# Create your views here.
# 멘토 멘티를 따로 데이터를 저장해줘야할꺼같은데.... 그 부분을 아직 못함....

def signup(request):
    if request.method == "POST":
        user_form = UserForm(request.POST)
        Profile_form = ProfileForm(request.POST)

        if all((user_form.is_valid(), Profile_form.is_valid())):
            user = user_form.save(commit=False)
            profile = Profile_form.save(commit=False)

            if request.POST.get('h-type') == '0':
                user.is_staff = True

            else:
                user.is_staff = False
            
            if request.POST.get('gender')=='0':
                profile.female = True

            else:
                profile.female = False

            user.save()
            profile.user = user
            profile.save()
            login(request, user)
            
            return redirect('index')

        else:
            return HttpResponse('사용자명이 이미 존재합니다.')

    else:
        user_form = UserForm()
        profile_form = ProfileForm()

        return render(request, 'signup.html',  {
            'user_form': user_form,
            "profile_form": profile_form
            })


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
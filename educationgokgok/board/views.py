from django.shortcuts import render

# Create your views here.

def new(request):
    return render(request, 'new.html')

def detail(request):
    return render(request, 'detail.html')

def board_main(request):
    return render(request, 'board_main.html')

def board_major(request):
    return render(request, 'board_major.html')

def board_local(request):
    return render(request, 'board_local.html')
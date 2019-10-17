from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                context = {
                    'page_title': 'Create new account',
                    'error': 'Username already exist',
                }
                return render(request, 'account/signup.html', context)
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
                auth.login(request, user)
                return redirect('home')
        else:
            context = {
                'page_title': 'Create new account',
                'error': 'Password mismatch',
            }
            return render(request, 'account/signup.html', context)
    else:
        context = {
            'page_title': 'Create new account',
        }
        return render(request, 'account/signup.html', context)

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            context = {
                'page_title': 'Login to your account',
                'error': 'Invalid User',
            }
            return render(request, 'account/login.html', context)
    else:
        context = {
            'page_title': 'Login to your account',
        }
        return render(request, 'account/login.html', context)

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('login')

from django.shortcuts import render

def signup(request):
    if request.method == 'POST':
        pass
    else:
        pass
    context = {
        'page_title': 'Create new account',
    }
    return render(request, 'account/signup.html', context)

def login(request):
    context = {
        'page_title': 'Login to your account',
    }
    return render(request, 'account/login.html', context)

def logout(request):
    pass

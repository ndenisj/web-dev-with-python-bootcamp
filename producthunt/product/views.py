from django.shortcuts import render

def home(request):
    context = {
        'page_title': 'Welcome to product hunt',
    }
    return render(request, 'product/home.html', context)

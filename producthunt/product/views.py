from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Product

def home(request):
    context = {
        'page_title': 'Welcome to product hunt',
    }
    return render(request, 'product/home.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        product = Product()
        product.title = request.POST['title']
        product.body = request.POST['body']
        product.icon = request.FILES['icon']
        product.image = request.FILES['image']
        if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
            product.url = request.POST['url']
        else:
            product.url = 'htt://' + request.POST['url']
        product.hunter = request.user

        ################
        #product.pub_date = timezone.datetime.now()
        #product.votes_total = 1
        product.save()
        #redirect to details
        return redirect('home')
    else:
        context = {
            'page_title': 'Create new product',
        }
        return render(request, 'product/create.html', context)

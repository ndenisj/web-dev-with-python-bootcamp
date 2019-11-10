from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Product


def home(request):
    products = Product.objects.all()
    context = {
        'page_title': 'Welcome to product hunt',
        'products': products,
    }
    return render(request, 'product/home.html', context)


@login_required(login_url='login')
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
        # product.pub_date = timezone.datetime.now()
        # product.votes_total = 1
        product.save()
        # redirect to details
        return redirect('home')
    else:
        context = {
            'page_title': 'Create new product',
        }
        return render(request, 'product/create.html', context)


@login_required(login_url='login')
def list(request):
    user = request.user
    products = Product.objects.filter(hunter=user)
    context = {
        'page_title': 'My products',
        'products': products,
    }
    return render(request, 'product/list.html', context)


@login_required(login_url='login')
def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'page_title': 'Product detail',
        'product': product,
    }
    return render(request, 'product/detail.html', context)


@login_required(login_url='login')
def edit(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        product.title = request.POST['title']
        product.body = request.POST['body']
        if 'icon' in request.FILES:
            product.icon = request.FILES['icon']
        if 'image' in request.FILES:
            product.image = request.FILES['image']
        if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
            product.url = request.POST['url']
        else:
            product.url = 'htt://' + request.POST['url']
        # product.hunter = request.user

        ################
        # product.pub_date = timezone.datetime.now()
        # product.votes_total = 1
        product.save()
        # redirect to details
        return redirect('home')
    else:
        context = {
            'page_title': 'Edit product',
            'product': get_object_or_404(Product, pk=product_id)
        }
        return render(request, 'product/edit.html', context)


@login_required(login_url='login')
def upvote(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        product.votes_total += 1
        product.save()
        return redirect('/product/' + str(product.id))


@login_required(login_url='login')
def delete(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        product.delete()
        return redirect('list')


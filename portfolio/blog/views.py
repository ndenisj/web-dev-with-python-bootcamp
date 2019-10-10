from django.shortcuts import render, get_object_or_404
from .models import Blog

def allblogs(request):
    blogs = Blog.objects.all()
    context = {
        'blogs' : blogs
    }
    return render(request, 'blog/allblogs.html', context)

def detail(request, blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id)
    context = {
        'blog': detailblog
    }
    return render(request, 'blog/detail.html', context)

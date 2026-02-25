from django.shortcuts import render
from .models import Blog
# Create your views here.
from django.shortcuts import render
from .models import Blog

def blog(request):
    blogs = Blog.objects.all().order_by('-id')
    return render(request, 'blog.html', {'blogs': blogs})

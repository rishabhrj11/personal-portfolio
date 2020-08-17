from django.shortcuts import render
from .models import Blog
def blog(request):
    blogs = Blog.objects.order_by('date')[:5]
    return render(request,'blogs/blog.html',{"blogs":blogs})

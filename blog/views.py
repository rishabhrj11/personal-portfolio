from django.shortcuts import render,get_object_or_404
from .models import Blog
def blog(request):
    blogs = Blog.objects.order_by('date')[:5]
    return render(request,'blogs/blog.html',{"blogs":blogs})

def detail(request,blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    return render(request,'blogs/detail.html',{'blog':blog})

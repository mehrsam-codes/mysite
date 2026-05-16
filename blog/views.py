from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from blog.models import Post
# Create your views here.
def blog_view(request):
    Posts = Post.objects.filter(status=1)
    context = {'posts': Posts}
    return render(request , 'blog/blog-home.html' , context)

def blog_single(request):
    return render(request , 'blog/blog-single.html')
def test(request):
    Posts = Post.objects.all()
    context = {'posts': Posts}
    return render(request , 'test.html' ,context )
    
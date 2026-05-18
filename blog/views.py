from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse , JsonResponse
from blog.models import Post
# Create your views here.
def blog_view(request ,**kwargs):
    Posts = Post.objects.filter(status=1)
    print(kwargs)   
    if kwargs.get('cat_name') != None:
        Posts = Posts.filter(category__name = kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        Posts = Posts.filter(author__username = kwargs['author_username'])
    context = {'posts': Posts}
    return render(request , 'blog/blog-home.html' , context)

def blog_single(request , pid):
    post = get_object_or_404(Post , pk=pid , status=1)
    context = {'post': post}
    return render(request , 'blog/blog-single.html' , context)
def test(request , pid):
    # post = Post.objects.get(id=pid)
    post = get_object_or_404(Post , pk=pid)
    context = {'post': post}
    return render(request , 'test.html' ,context )
from django.shortcuts import render

def test_view(request):
    return render(request, 'test.html')
def  blog_category(request , cat_name):
    posts = Post.objects.filter(status = 1)
    posts = posts.filter(category__name = cat_name)
    context = {'posts':posts}
    return render(request , 'blog/blog-home.html' , context)
def blog_search(request):
    Posts = Post.objects.filter(status=1)
    # print(request.__dict__)
    if request.method == 'GET':
        if s:= request.GET.get('s'):
            Posts = Posts.filter(content__contains=s)
    context = {'posts': Posts}
    return render(request , 'blog/blog-home.html' , context)
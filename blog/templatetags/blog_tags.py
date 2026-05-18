from django import template
from blog.models import Post , Category
register = template.Library()
@register.simple_tag(name='posts')
def posts():
    return Post.objects.filter(status=1)

@register.simple_tag(name='totalposts')
def totalposts():
    return Post.objects.filter(status=1).count()

@register.filter
def snippet(text  , arg=20):
    return text[:arg] + '...'
@register.inclusion_tag('blog/popular-posts.html')
def latestposts(arg):
    posts = Post.objects.filter(status=1).order_by('published_date')[:arg]
    return {'posts':posts}

@register.inclusion_tag('blog/post-categories.html')
def postcategories():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(category = name).count
    return {'categories':cat_dict}
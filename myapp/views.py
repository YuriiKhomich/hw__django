
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from myapp.models import BlogPost


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def main(request):
     blog_posts = BlogPost.objects.all()
     return render(request, 'main.html', {'blog_posts': blog_posts})


def blog_detail(request, slug):
    blog_post = get_object_or_404(BlogPost, slug=slug)
    comments = blog_post.comments.all()
    return render(request, 'blog_detail.html', {'blog_post': blog_post, 'comments': comments})


def create(request):
    return render(request, 'create_blog.html')


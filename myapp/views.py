from django.shortcuts import render, get_object_or_404
from .models import Topic, Blog


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def main(request):
    blogs = Blog.objects.all()
    return render(request, 'main.html', {'blogs': blogs})


def blog_detail(request):
    return render(request, 'blog_detail.html')


def topic_detail(request, slug):
    topic = get_object_or_404(Topic, slug=slug)
    comments = topic.comments.all()
    return render(request, 'topic_detail.html', {'topic': topic, 'comments': comments})


def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    topics = blog.topics.all()
    return render(request, 'blog_detail.html', {'blog': blog, 'topics': topics})


def create(request):
    return render(request, 'create_blog.html')

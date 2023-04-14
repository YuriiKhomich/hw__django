
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def main(request):
    return render(request, 'main.html')


def blog_detail(request, name=''):
    return render(request, 'blog_detail.html')


def create(request):
    return render(request, 'create_blog.html')


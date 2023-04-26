from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from .models import BlogPost, Topic
from .forms import BlogPostForm, CommentForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('main')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            auth_login(request, user)
            return redirect('main')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


@login_required
def main(request):
    blogs = BlogPost.objects.all()
    topics = Topic.objects.all()
    return render(request, 'main.html', {'blogs': blogs, 'topics': topics})


def blog_detail(request, slug):
    blog_post = get_object_or_404(BlogPost, slug=slug)
    comments = blog_post.comments.all()
    return render(request, 'blog_detail.html', {'blog_post': blog_post, 'comments': comments})


def blogs_by_topic(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    blogs = BlogPost.objects.filter(topics__id=topic_id)
    return render(request, 'blogs_by_topic.html', {'topic': topic, 'blogs': blogs})


def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            form.save_m2m()
            return redirect('blog_post_detail', slug=blog_post.slug)
    else:
        form = BlogPostForm()
    return render(request, 'create_blog_post.html', {'form': form})


def blog_post_detail(request, slug):
    blog_post = get_object_or_404(BlogPost, slug=slug)
    comments = blog_post.comments.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.blog_post = blog_post
            comment.save()
            return redirect('blog_post_detail', slug=slug)
    else:
        form = CommentForm()
    
    context = {
        'blog_post': blog_post,
        'comments': comments,
        'form': form,
    }
    return render(request, 'blog_detail.html', context)


def create(request):
    return render(request, 'create_blog.html')


def search_blog_posts(request):
    query = request.GET.get('q', '')
    if query:
        blog_posts = BlogPost.objects.filter(Q(title__icontains=query))
    else:
        blog_posts = BlogPost.objects.all()

    return render(request, 'search_blog_posts.html', {'blog_posts': blog_posts})

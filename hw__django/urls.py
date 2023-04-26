from django.urls import path
import myapp.views
from django.contrib import admin
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('blog/<slug:slug>/', myapp.views.blog_post_detail, name='blog_post_detail'),
    path('', myapp.views.index, name='index'),
    path('login/', myapp.views.login, name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', myapp.views.register, name='register'),
    path('main/', myapp.views.main, name='main'),
    path('blog/', myapp.views.blog_detail, name='blog_detail'),
    path('create_blog', myapp.views.create, name='create_blog'),
    path('blogs/topic/<int:topic_id>/', myapp.views.blogs_by_topic, name='blogs_by_topic'),
    path('search/', myapp.views.search_blog_posts, name='search_blog_posts'),
    path('create_blog_post/', myapp.views.create_blog_post, name='create_blog_post'),
    ]
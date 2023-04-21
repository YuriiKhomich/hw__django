from django.urls import path
import myapp.views
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('', myapp.views.index, name='index'),
    path('login/', myapp.views.login, name="login"),
    path('register/', myapp.views.register, name='register'),
    path('main/', myapp.views.main, name='main'),
    path('blog/<int:blog_id>/', myapp.views.blog_detail, name='blog_detail'),
    path('topic/<slug:slug>/', myapp.views.topic_detail, name='topic_detail'),
    path('create_blog', myapp.views.create, name='create_blog')
    ]
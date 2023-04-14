from django.urls import path
import myapp.views

urlpatterns = [
    path('', myapp.views.index, name='index'),
    path('login/', myapp.views.login, name="login"),
    path('register/', myapp.views.register, name='register'),
    path('main/', myapp.views.main, name='main'),
    path('blog/', myapp.views.blog_detail, name='blog_detail'),
    path('create_blog', myapp.views.create, name='create_blog')
    ]
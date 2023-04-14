from django.urls import path
import myapp.views
urlpatterns = [
    path('<slug:name>/', myapp.views.blog_detail, name='blog_detail'),
    path('<slug:name>/comment/', myapp.views.add_comment_to_post, name='add_comment_to_post'),
    path('<slug:name>/update/', myapp.views.blog_update, name='blog_update'),
    path('<slug:name>/delete/', myapp.views.blog_delete, name='blog_delete'),
    path('<str:username>/', myapp.views.profile, name='profile'),
    path('<str:username>/change_password/', myapp.views.change_password, name='change_password'),
    ]
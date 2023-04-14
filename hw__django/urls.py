from django.urls import path, include
import myapp.views

urlpatterns = [
    path('', myapp.views.blogs),
    path('blogs/', myapp.views.blogs, name='blogs'),
    path('about/', myapp.views.about),
    path('create/', myapp.views.create, name='create'),
    path('profile/', include('myapp.urls')),
    path('register/', myapp.views.register),
    path('login/', myapp.views.login),
    path('logout/', myapp.views.blogs),
    path('blog/', include('myapp.urls'))
    ]

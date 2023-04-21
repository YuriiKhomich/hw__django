from django.contrib import admin
from .models import Topic, Blog, Comment


admin.site.register(Topic)
admin.site.register(Blog)
admin.site.register(Comment)

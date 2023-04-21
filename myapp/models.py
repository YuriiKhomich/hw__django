from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class Topic(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    users = models.ManyToManyField(User, related_name='topics', blank=True)
    notify = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title

    
class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    topics = models.ManyToManyField(Topic, related_name='blog_posts')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, max_length=255, blank=True)
    
    def __str__(self):
        return self.title
    
    def _generate_unique_slug(self):
        slug = f"{slugify(self.title)}-{datetime.now().strftime('%Y-%m-%d')}"
        unique_slug = slug
        num = 1

        while BlogPost.objects.filter(slug=unique_slug).exists():
            unique_slug = f"{slug}-{num}"
            num += 1

        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._generate_unique_slug()
        super().save(*args, **kwargs)


class Comment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    
    def __str__(self):
        return self.content

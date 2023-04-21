from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.urls import reverse


class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogs')

    def __str__(self):
        return self.title

    
class Topic(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='topics')
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, max_length=255, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        if not self.slug:
            slug = f"{slugify(self.title)}-{self.created_at.strftime('%Y-%m-%d')}"
            unique_slug = slug
            counter = 1
            while Topic.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{slug}-{counter}"
                counter += 1
            self.slug = unique_slug
            super().save(update_fields=['slug'])

    def get_absolute_url(self):
        return reverse('topic_detail', args=[str(self.slug)])
    
    class Meta:
        db_table = 'myapp_new_topic'


class Comment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='comments')
    
    class Meta:
        db_table = 'myapp_new_comment'

    def __str__(self):
        return self.content

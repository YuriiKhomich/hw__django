# Generated by Django 4.2 on 2023-04-17 12:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0004_comment_blog_post_comment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='author',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blogpost',
            name='topics',
            field=models.ManyToManyField(related_name='blog_posts', to='myapp.topic'),
        ),
        migrations.AddField(
            model_name='topic',
            name='notify',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='topic',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='topics', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True),
        ),
    ]

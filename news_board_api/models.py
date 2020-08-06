from datetime import datetime
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    link = models.URLField(max_length=200)
    creation_date = models.DateTimeField(default=datetime.now, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    user_upvote = models.ManyToManyField(User, related_name='upvote')


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)
    creation_date = models.DateTimeField(default=datetime.now, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

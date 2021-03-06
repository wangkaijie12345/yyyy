from django.db import models
from django.utils import timezone


# Create your models here.


class Article(models.Model):
    STATUS_CHOICE = (('published', '发表'), ('draft', '草稿'))
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique_for_date='publish', default="1")
    clicks = models.IntegerField(default=0)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICE, default='draft')

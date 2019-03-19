from django.db import models
from django.utils import timezone
from django.urls import reverse
from uuslug import slugify


# Create your models here.
class Post(models.Model):
    STATUS_CHOICES = (
        (-1, "删除"),
        (0, '草稿'),
        (1, '发表'),
        (2, '热门'),
        (3, '推荐'),
    )
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, unique_for_date='publish', default="1")
    clicks = models.PositiveIntegerField(default=0)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now())
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.SmallIntegerField(max_length=10, choices=STATUS_CHOICES, default=0)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail',
                       args=[
                           self.publish.year,
                           self.publish.month,
                           self.publish.day,
                           self.slug
                       ])

    def increase_views(self):
        self.clicks += 1
        self.save(update_fields=['clicks'])

    def save(self, **kwargs):
        self.slug = slugify(self.title)
        super().save(**kwargs)

from django.db import models
from django.utils import timezone
from uuslug import slugify
from django.urls import reverse


# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    clicks = models.PositiveIntegerField(default=0)
    publish = models.DateField(default=timezone.now())
    slug = models.SlugField(max_length=250, unique_for_date='publish',
                            default=1)
    STATUS_CHOICE = ((-1, '删除'), (0, '草稿'), (1, '发表'), (2, '热门'))
    status = models.SmallIntegerField(max_length=10, choices=STATUS_CHOICE,
                                      default=0)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('post_detail',
    #                    args=[
    #                        self.publish.year,
    #                        self.publish.month,
    #                        self.publish.day,
    #                        self.slug
    #                    ])

    def save(self, **kwargs):
        self.slug = slugify(self.title)
        super().save(**kwargs)

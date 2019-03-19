from django.contrib import admin
from .models import Article


# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'publish', 'status', 'create',)
    # 右侧过滤列表侧边栏


#

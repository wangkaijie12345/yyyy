from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('article/create/', views.ArticleCreate.as_view(), name='create_article'),
    path('article/update/<pk>/', views.ArticleUpdate.as_view(), name='update_article'),
    path('article/del/<pk>/',views.ArticleDel.as_view(),name='article_del'),

]

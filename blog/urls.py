from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('article/list/', views.ArticleList.as_view(),name='article_list'),
    path('article/detail/<pk>/',views.ArticleDetail.as_view(),name='article_detail'),
    path('article/delete/<int:id>/',views.article_delete,name='article_delete'),
    path('article/create/',views.ArticleCreate.as_view(),name='article_create'),
    path('article/update/<pk>/',views.ArticleUpdate.as_view(),name='article_update')
]
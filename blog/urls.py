from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/create/', views.PostCreate.as_view(), name='post_create'),
path('post/<year>/<month>/<day>/<slug>/',views.PostDetail.as_view(),name='post_detail'),

]

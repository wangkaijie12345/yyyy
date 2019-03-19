from django.shortcuts import render
from .models import Article
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.

def index(request):
    article = Article.objects.all()
    return render(request, 'article/index.html', {'article': article})


class ArticleCreate(CreateView):
    model = Article
    fields = ('title', 'body',)
    template_name = 'article/article_create.html'
    success_url = reverse_lazy('index')


class ArticleUpdate(UpdateView):
    model = Article
    fields = ('title', 'body',)
    template_name = 'article/article_update.html'
    success_url = reverse_lazy('index')


class ArticleDel(DetailView):
    model = Article
    template_name = 'article/article_del.html'
    success_url = reverse_lazy('index')

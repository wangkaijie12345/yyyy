from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Article
from django.urls import reverse_lazy
# Create your views here.
def index(request):
    return render(request,'index.html')

class ArticleList(ListView):
    model = Article
    template_name = 'article_list.html'

class ArticleDetail(DetailView):
    model = Article
    template_name = 'article_detail.html'

def article_delete(request,id):
    article=Article.objects.get(id=id)
    article.delete()
    return redirect('article_list')

class ArticleCreate(CreateView):
    model = Article
    fields = ('title','slug','body')
    template_name = 'article_create.html'
    success_url = reverse_lazy('article_list')

class ArticleUpdate(UpdateView):
    model = Article
    fields = ('title','body')
    template_name = 'article_update.html'
    success_url = reverse_lazy('article_list')
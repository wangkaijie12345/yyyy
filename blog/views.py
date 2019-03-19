from django.shortcuts import render
from .models import Post
from django.views.generic import CreateView, DeleteView
from django.utils import timezone

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'post/index.html', {'posts': posts})


def post_delete(request,id):
    post=Post.objects.get(id=id)
    post.delete()
    return render(request,'post/index.html')

class PostCreate(CreateView):
    model = Post
    fields = ('title', 'body', 'status')
    template_name = 'post/post_create.html'

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        form.instance.publish = timezone.now()
        return super().form_valid(form)













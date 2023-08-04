from django.shortcuts import render
from .models import Post
# Create your views here.
def home(request):

    posts = Post.objects.all()
    context = {
        'posts': posts
    }

    return render(request=request, template_name='blog/home.html', context=context)

def post_datail(request, post_id):
    post = Post.objects.get(pk=post_id)

    context = {
        'post': post,
    }

    return render(request=request,template_name='blog/post_datail.html', context=context)

from django.shortcuts import render, redirect
from  django.http import HttpResponse, Http404
import logging
from .models import Post

## static data
# posts = [
#         {'id':1, 'title': 'post1', 'content': 'content of the post 1'},
#         {'id':2,'title': 'post2', 'content': 'content of the post 2'},
#         {'id':3,'title': 'post3', 'content': 'content of the post 3'},
#         {'id':4,'title': 'post4', 'content': 'content of the post 4'},
#     ]

def index(request):
    posts = Post.objects.all()
    blog_title = "Latest Posts"    
    return render(request, 'blog/index.html', {'blog_title': blog_title, 'posts': posts})

def detail(request, post_id):
    # post = next((item for item in posts if item['id']==post_id), None)   # static data

    posts = Post.objects.all()
    
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    
    # logger = logging.getLogger('TESTING')
    # logger.debug(f"post is available {post}")
    return render(request, 'blog/detail.html', {'post':post, 'posts':posts})

def old_url_redirect(requset):
    return redirect("blog:new_url")

def new_url_view(request):
    return HttpResponse("This is new url")

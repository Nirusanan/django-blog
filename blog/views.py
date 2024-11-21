from django.shortcuts import render, redirect
from  django.http import HttpResponse


def index(request):
    blog_title = "Latest Posts"
    posts = [
        {'id':1, 'title': 'post1', 'content': 'content of the post 1'},
        {'id':2,'title': 'post2', 'content': 'content of the post 2'},
        {'id':3,'title': 'post3', 'content': 'content of the post 3'},
        {'id':4,'title': 'post4', 'content': 'content of the post 4'},
    ]
    return render(request, 'blog/index.html', {'blog_title': blog_title, 'posts': posts})

def detail(request, post_id):
    return render(request, 'blog/detail.html')

def old_url_redirect(requset):
    return redirect("blog:new_url")

def new_url_view(request):
    return HttpResponse("This is new url")

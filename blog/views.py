from django.shortcuts import render, redirect
from  django.http import HttpResponse, Http404
import logging
from .models import Post, AboutUs
from django.core.paginator import Paginator
from .forms import ContactForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required

## static data
# posts = [
#         {'id':1, 'title': 'post1', 'content': 'content of the post 1'},
#         {'id':2,'title': 'post2', 'content': 'content of the post 2'},
#         {'id':3,'title': 'post3', 'content': 'content of the post 3'},
#         {'id':4,'title': 'post4', 'content': 'content of the post 4'},
#     ]

@login_required(login_url='/')
def index(request):
    all_posts = Post.objects.all()
    blog_title = "Latest Posts"    

    # pagination
    paginator = Paginator(all_posts, 5)
    page_num = request.GET.get('page')
    page_posts =  paginator.get_page(page_num)

    return render(request, 'blog/index.html', {'blog_title': blog_title, 'page_posts': page_posts})


def detail(request, slug):
    # post = next((item for item in posts if item['id']==post_id), None)   # static data

    posts = Post.objects.all()
    
    try:
        post = Post.objects.get(slug=slug)
        related_posts = Post.objects.filter(category = post.category).exclude(pk=post.id)
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    
    # logger = logging.getLogger('TESTING')
    # logger.debug(f"post is available {post}")
    return render(request, 'blog/detail.html', {'post':post, 'related_posts':related_posts})

def old_url_redirect(requset):
    return redirect("blog:new_url")

def new_url_view(request):
    return HttpResponse("This is new url")


@login_required(login_url='/')
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        name= request.POST.get('name')
        email= request.POST.get('email')
        message= request.POST.get('message')
        
        logger = logging.getLogger('TESTING')

        if form.is_valid():
            logger.debug(f"Conatct Post data is {form.cleaned_data['name']} {form.cleaned_data['email']} {form.cleaned_data['message']}")
            success_message = "Your message has been sent!"
            return render(request, 'blog/contact.html', {'form': form, 'success_message': success_message})

        else:
           logger.debug("Form validation failure")
        return render(request, 'blog/contact.html', {'form': form, 'name':name, 'email':email, 'message':message})
    
    return render(request, 'blog/contact.html')


def aboutus_view(requset):
    about_content = AboutUs.objects.first().content
    return render(requset, "blog/about.html", {'about_content': about_content})


def signup(request):
    if request.method == 'POST':
        fnm=request.POST.get('name')
        emailid=request.POST.get('email')
        pwd=request.POST.get('pwd')
        my_user=User.objects.create_user(fnm,emailid,pwd)
        my_user.save()
        return redirect('/blog')
    
    return render(request, 'blog/signup.html')


def login(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        pwd=request.POST.get('pwd')
        print(name,pwd)
        userr=authenticate(request, username=name, password=pwd)
        if userr is not None:
            auth_login(request,userr)
            return redirect('/blog')
        else:
            return redirect('/')
               
    return render(request, "blog/login.html")


def signout(request):
    logout(request)
    return redirect('/')


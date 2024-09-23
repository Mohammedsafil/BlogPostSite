from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
import logging
from .models import Post
from django.http import Http404

# Create your views here.
# posts = [
#         {'id': 1,'title': 'Post1', 'content': 'Post content 1'},
#         {'id': 2,'title': 'Post2', 'content': 'Post content 2'},
#         {'id': 3,'title': 'Post3', 'content': 'Post content 3'},
#         {'id': 4,'title': 'Post4', 'content': 'Post content 4'}
#     ]



def index(request):
    blog_title = "Lastest Posts By Safil"
    posts = Post.objects.all()
    return render(request,"index.html",{'Blog_title' : blog_title, 'posts' : posts})

def detail(request, post_id):
    # post = next((iteam for iteam in posts if int(post_id) == iteam['id']), None)
    # logger = logging.getLogger("TESTING")
    # logger.debug(f'Post variable is {post}')
    try:
        post = Post.objects.get(pk=post_id)
    
    except Post.DoesNotExist:
        raise Http404("Page Does not exist!")
    
    return render(request,"details.html",{'post':post})

def old_url(request):
    return redirect(reverse("blog:new_page"))

def new_url(request):
    return HttpResponse("In New Url Page")
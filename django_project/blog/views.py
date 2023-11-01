from django.shortcuts import render
from django.http import HttpResponse 
from .models import Post

def home(request): 
    '''
    this is the logic for how we want to handle when the user wants to go to the homepage.
    We haven't mapped the URL to this function, so we create a urls.py to map it.

    Why isn't the urls.py auto-generated?
    - https://stackoverflow.com/questions/59480290/why-is-the-urls-py-file-not-created-automatically
    - TLDR: sometimes app only does internal things, urls.py is only useful for routing users to pages specific to the app

    There are a couple of ways we can load in a template:
    1. load template in, render it, pass it as HttpResponse 
    2. Django also has a shortcut to do ^ 
    '''
    posts = Post.objects.all()

    context = {
        'posts':  posts
    }

    #return HttpResponse('<h1>Blog Home</h1>') 
    return render(request, 'blog/home.html', context)

def about(request): 
    return render(request, 'blog/about.html', {'title':'About'})
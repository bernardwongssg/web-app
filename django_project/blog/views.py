from django.shortcuts import render
from django.http import HttpResponse 


posts = [
    {
        'author': 'Bernie',
        'title': 'Blog Post 1',
        'content': 'first post content',
        'date_posted': '10.28.23',
    }, 
    {
        'author': 'Bdub',
        'title': 'Blog Post 2',
        'content': 'first post content go crazy',
        'date_posted': '10.28.23',
    }
]

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
    context = {
        'posts':  posts
    }

    #return HttpResponse('<h1>Blog Home</h1>') 
    return render(request, 'blog/home.html', context)

def about(request): 
    return render(request, 'blog/about.html', {'title':'About'})
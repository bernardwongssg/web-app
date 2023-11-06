from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse 
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


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

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    # this will be looking for blog/post_detail.html
    # items from this model will be referenced with the keyword 'object'
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    # this will be looking for blog/post_form.html
    # items from this model will be referenced with the keyword 'object'
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        '''
        you do this before saving the form, b/c the author isn't set yet 
        you can do this when validating the form. That's why you override form_valid()
        instead of save() 
        '''
        # before you set the form, set the author 
        form.instance.author = self.request.user 
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    # this will be looking for blog/post_form.html
    # items from this model will be referenced with the keyword 'object'
    # NOTE: while the code is pretty similar to PostCreateView, you should add in extra validation to make sure the author is valid
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        '''
        you do this before saving the form, b/c the author isn't set yet 
        you can do this when validating the form. That's why you override form_valid()
        instead of save() 
        '''
        # before you set the form, set the author 
        form.instance.author = self.request.user 
        return super().form_valid(form)

    def test_func(self):
        '''
        used by UserPassesTestMixin
        '''
        post = self.get_object() # gets the post that we're currently trying to update 
        return self.request.user == post.author # if current logged in user is equal to post author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        '''
        used by UserPassesTestMixin
        '''
        post = self.get_object() # gets the post that we're currently trying to update 
        return self.request.user == post.author # if current logged in user is equal to post author

    

    

def about(request): 
    return render(request, 'blog/about.html', {'title':'About'})


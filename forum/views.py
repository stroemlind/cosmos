from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post
from .forms import PostForm

# Create your views here.
class PostList(generic.ListView):
    """
    The class to display all the post in the forum
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class PostDetailView(generic.DetailView):
    """
    The class to display the post in detail
    """
    model = Post
    template_name = 'post_detail.html'


class AddPost(generic.CreateView):
    """
    The class to display text editor for users to create post
    """
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = ('title', 'slug', 'author', 'image', 'content', 'status')


class EditPost(generic.UpdateView):
    """
    The class to edit a post
    """
    model = Post
    template_name = 'edit_post.html'
    fields = ['title', 'slug', 'image', 'content']

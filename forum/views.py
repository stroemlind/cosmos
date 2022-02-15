from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post

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

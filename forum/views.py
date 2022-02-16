from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
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


#class PostDetailView(generic.DetailView):
    #model = Post
    #template_name = 'post_detail.html'


def get_post(request, pk):
    """
    Function to se a post in detail
    """
    post = get_object_or_404(Post, pk=pk)
    template = 'post_detail.html'
    context = {
        'post': post
    }
    return render(request, template, context)

# class AddPost(generic.CreateView):
    # """
    # The class to display text editor for users to create post
    # """
    # model = Post
    # form_class = PostForm
    # template_name = 'add_post.html'


def add_post(request):
    """
    Function to add a post to the forum
    """
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        # context['posted'] = form.instance
        if form.is_valid():
            post = form.save()
            post_id = post.pk
            return redirect(get_post, post_id)
    else:
        form = PostForm()
    context = {
        'form': form
    }
    return render(request, 'add_post.html', context)


class EditPost(generic.UpdateView):
    """
    The class to edit a post
    """
    model = Post
    template_name = 'edit_post.html'
    fields = ['title', 'slug', 'image', 'content']


class DeletePost(generic.DeleteView):
    """
    The class to delete a post
    """
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

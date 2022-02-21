from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Post, Category
from .forms import PostForm

# Create your views here.
class PostList(generic.ListView):
    """
    The class to display all the post in the forum
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 12

    # def get_context_data(self, *args, **kwargs):
    #     category_menu = Category.objects.all()
    #     context = super(PostList, self).get_context_data(*args, **kwargs)
    #     context['category_menu'] = category_menu
    #     return context


def get_post(request, pk):
    """
    Function to view a post in detail and get likes
    """
    post = get_object_or_404(Post, pk=pk)
    template = 'post_detail.html'
    number_of_likes = post.number_of_likes()
    liked = False
    if request.method == 'POST':
        if post.likes.filter(id=post.request.user.id).exists():
            liked = True
            return liked
    context = {
        'post': post,
        'liked': liked,
        'number_of_likes': number_of_likes,
    }
    return render(request, template, context)


def category_page(request, categories):
    """
    Function to view each category on its own page
    """
    category_posts = Post.objects.filter(category=categories)
    template = 'category.html'
    return render(request, template, {
        'categories': categories,
        'category_posts': category_posts}
        )


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
    fields = ['title', 'image', 'content']


class DeletePost(generic.DeleteView):
    """
    The class to delete a post
    """
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


class LikeView(View):
    """
    The view for likes
    """
    def post(self, request, pk, *args, **kwargs):
        """
        The function to determine the view if a user has liked a post or not
        """
        post = get_object_or_404(Post, pk=pk)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post-detail', args=[pk]))

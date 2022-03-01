from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.db.models import Count
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Post, Category
from .forms import PostForm, CommentForm


def home_view(request):
    """
    The view function to display a list of all the post made with newest
    one first. Alls sets the links in the category navbar
    """
    post = Post.objects.filter(status=1).order_by('-created_on')
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category']
            post = post.filter(category__in=categories)
            categories = Category.objects.filter(category_name__in=categories)

        context = {
            'post': post,
            'current_categories': categories,
        }
        return render(request, 'category.html', context)

    context = {
        'post': post,
        'current_categories': categories,
    }

    return render(request, 'index.html', context)


def get_post(request, pk):
    """
    Function to view a post in detail, give likes and view comments.
    """
    post = get_object_or_404(Post, pk=pk)
    template = 'post_detail.html'
    comments = post.comments.filter(approved=True).order_by('-created_on')
    number_of_likes = post.number_of_likes()
    liked = False
    if request.method == 'POST':
        if post.likes.filter(id=post.request.user.id).exists():
            liked = True
            return liked

    context = {
        'post': post,
        'comments': comments,
        'liked': liked,
        'number_of_likes': number_of_likes,
        'CommentForm': CommentForm()
    }
    return render(request, template, context)


def category_page(request):
    """
    Function to view each category on its own page
    """
    category = request.GET.get("category")
    category_post = Post.objects.filter(category=category)
    template = 'category.html'
    return render(request, template, {
        'category': category,
        'category_post': category_post,
        }
    )


@login_required
def add_post(request):
    """
    Function to add a post to the forum
    """
    user = get_object_or_404(User, username=request.user)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.author = user
            post = form.save()
            post_id = post.pk
            return redirect(get_post, post_id)
    else:
        form = PostForm()
    context = {
        'form': form
    }
    return render(request, 'add_post.html', context)


@login_required
def add_comment(request, pk):
    """
    Function view to add comment to a post
    """
    post = get_object_or_404(Post, pk=pk)
    comment_form = CommentForm()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST, request.FILES)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post-detail', pk)
    context = {
        'comment_form': comment_form,
        'post': post,
    }
    return render(request, 'add_comment.html', context)


class EditPost(generic.UpdateView):
    """ test """
    model = Post
    template_name = 'edit_post.html'
    fields = [
        'title',
        'image',
        'content',
    ]


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


class MostLikedPost(generic.ListView):
    """
    The function for the 'Most Populare Post' view
    """
    model = Post
    queryset = Post.objects.filter(status=1).annotate(
        like_count=Count('likes')).order_by('-like_count')
    template_name = 'popular_post.html'
    paginate_by = 15

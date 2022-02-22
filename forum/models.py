from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from cloudinary.models import CloudinaryField
from tinymce.models import HTMLField


# Create your models here.
STATUS = ((0, 'Draft'), (1, 'Published'))

class Category(models.Model):
    """
    The model for all the categories
    """
    category_name = models.CharField(max_length=40, default='none')

    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        return reverse('home')

class Post(models.Model):
    """
    The class based model for the post function of the forum
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='forum_posts'
    )
    category = models.CharField(max_length=40, default='none')
    image = CloudinaryField('image', default='placeholder')
    updated_on = models.DateTimeField(auto_now=True)
    content = HTMLField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='forum_post_like', blank=True)

    class Meta:
        """
        Class to order the newest post created to apper first
        """
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')

    def number_of_likes(self):
        """
        Counting and returning the numer of likes a post has
        """
        return self.likes.count()


class Comment(models.Model):
    """
    The class based model for Comments on the forums post
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='forum_comment')
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments')
    body = HTMLField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """
        Class to order the oldest post created to apper first
        """
        ordering = ['created_on']

    def __str__(self):
        return f'Comment: {self.body} By: {self.user}'

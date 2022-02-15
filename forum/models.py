from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from cloudinary.models import CloudinaryField
from tinymce.models import HTMLField


# Create your models here.
STATUS = ((0, 'Draft'), (1, 'Published'))


class Post(models.Model):
    """
    The class based model for the post function of the forum
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='forum_posts'
    )
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

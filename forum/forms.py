from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    """
    Class to style the form for creating a post for the forum
    """
    class Meta:
        """
        The Meta class with what will be displayed and widgets
        """
        model = Post
        fields = ('title', 'slug', 'author', 'image', 'content', 'status')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'})
        }

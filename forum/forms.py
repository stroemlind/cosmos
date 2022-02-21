from django import forms
from .models import Post, Category, Comment

choices = Category.objects.all().values_list('category_name', 'category_name')

choice_list = []

for choice in choices:
    choice_list.append(choice)


class PostForm(forms.ModelForm):
    """
    Class to style the form for creating a post for the forum
    """
    class Meta:
        """
        The Meta class with what will be displayed and widgets
        """
        model = Post
        fields = (
            'title',
            'slug',
            'author',
            'image',
            'category',
            'content',
            'status'
            )

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'hidden'}
                ),
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'value': '',
                'id': 'author-id',
                'type': 'hidden'
                }),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={
                'class': 'form-control'}
                ),
            'status': forms.Select(attrs={'class': 'form-control'})
        }


class CommentForm(forms.ModelForm):
    """ test """
    class Meta:
        """
        The Meta class with what will be displayed and widgets
        """
        model = Comment
        fields = ('body',)

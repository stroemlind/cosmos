from django.test import TestCase
from .forms import PostForm


class TestPostForm(TestCase):
    """ To test the code for PostForm """
    def test_title_is_unique(self):
        form = PostForm({'title': ''})
        self.assertFalse(form.is_valid())
        # self.assertIn('title', form.errors.keys())
        # self.assertEqual(form.errors['title'][0], 'This field is required')

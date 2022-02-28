from django.test import TestCase
from .models import Post, Comment, Category


class TestPostModel(TestCase):
    """
    Test the PostModel
    """
    @classmethod
    def setUpTestData(cls):
        Post.objects.create(
            title='Blog Post Test',
            slug='blog-post-test',
            author='TestUser',
            status='1',
            likes='True',
            )

    def test_status_default_published(self):
        """ Test if status is 1 when post are made """
        post = Post.objects.create(name='Test Post')
        self.assertEqual(post, 1)

    def test_title_max_length(self):
        """ test """
        post = Post.objects.get(id=1)
        max_length = post._meta.get_field('title').max_length
        self.assertEqual(max_length, 200)

    def test_slug_max_length(self):
        """ test """
        post= Post.objects.get(id=1)
        max_length = post_meta.get_field('slug').max_length
        self.assertEqual(max_length, 200)

    def test_slug_unique(self):
        """ test """
        post = Post.objects.get(id=1)
        response = self.client.get(reverse('post-detail', args=(post.slug,)))
        self.assertEqual(response.status_code, 200)

    def test_author_name(self):
        """ test """
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('author').verbose_name
        self.assertEqual(field_label, 'author')

    def test_object_title_str(self):
        """ test """
        post = Post.objects.get(id=1)
        expected_object_title = self.title
        self.assertEqual(str(post), expected_object_name)

    def test_get_absolute_url(self):
        """ test """
        post = Post.objects.get(id=1)
        self.assertEqual(post.get_absolute_url(), 'home')


class TestCommentModel(TestCase):
    """ Test Comment model """
    @classmethod
    def setUpTestData(cls):
        Comment.objects.create(
            user='TestUser',
            body='A test comment',
            approved='False',
            )

    def test_object_comment_body_by_user_str(self):
        """ test """
        comment = Comment.objects.get(id=1)
        expected_object_str = f'Comment: {self.body} By: {self.user}'
        self.assertEqual(str(comment), expected_object_str)

    def test_default_approved_are_false(self):
        """ test """
        comment = Comment.objects.get(id=1)
        self.assertFalse(comment.approved)


class TestCategoryModel(TestCase):
    """ Test the Category Model """
    @classmethod
    def setUpTestData(cls):
        Category.objects.create(
            category_name='TestCategory'
        )

    def test_get_absolute_url(self):
        """ test """
        category = Category.objects.get(id=1)
        self.assertEqual(category.get_absolute_url(), 'home')

    def test_category_name_max_length(self):
        """ test """
        category = Category.objects.get(id=1)
        max_length = category_meta.get_field('category_name').max_length
        self.assertEqual(max_length, 40)

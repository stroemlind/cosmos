from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment, Category


class TestPostModel(TestCase):
    """
    Test the PostModel
    """
    @classmethod
    def setUpTestData(cls):
        test_user1 = User.objects.create_user(
            username='testuser1',
            password='3E!uhGre09Wq'
            )

        test_user1.save()

        Post.objects.create(
            title='Test title',
            slug='test-title',
            author=test_user1,
            category='test',
            image='placeholder',
            updated_on='2022.02.28',
            content='test text body',
            created_on='2022.02.27',
            status=1,
            )

    def test_title_max_length(self):
        """ test """
        post = Post.objects.get(id=1)
        max_length = post._meta.get_field('title').max_length
        self.assertEqual(max_length, 200)

    def test_slug_max_length(self):
        """ test """
        post= Post.objects.get(id=1)
        max_length = post._meta.get_field('slug').max_length
        self.assertEqual(max_length, 200)

    def test_get_absolute_url(self):
        """ test """
        post = Post.objects.get(id=1)
        self.assertEqual(post.get_absolute_url(), '/')


class TestCommentModel(TestCase):
    """ Test Comment model """
    @classmethod
    def setUpTestData(cls):
        test_user1 = User.objects.create_user(
            username='testuser1',
            password='3E!uhGre09Wq'
            )

        test_user1.save()

        test_post = Post.objects.create(
            title='Test title',
            slug='test-title',
            author=test_user1,
            category='test',
            image='placeholder',
            updated_on='2022.02.28',
            content='test text body',
            created_on='2022.02.27',
            status=1,
            )

        test_post.save()

        Comment.objects.create(
            user=test_user1,
            post=test_post,
            body='test comment body',
            created_on='2022.02.28',
            approved='False'
        )

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
        self.assertEqual(category.get_absolute_url(), '/')

    def test_category_name_max_length(self):
        """ test """
        category = Category.objects.get(id=1)
        max_length = category._meta.get_field('category_name').max_length
        self.assertEqual(max_length, 40)

from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Post


# Create your tests here.
class TestViews(TestCase):
    """ Test the code for the views """
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
            # likes=likes.set(True)
            )

    def test_get_home_page(self):
        """ Test to get the right template for the view """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html', 'base.html')

    def test_get_get_post_page(self):
        """ Test to get the right template for the view """
        post = Post.objects.get(id=1)
        response = self.client.get(f'/post/{post.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail.html', 'base.html')

    def test_get_category_page_page(self):
        """ Test to get the right template for the view """
        response = self.client.get('/category/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'category.html', 'base.html')

    def test_get_mostlikedpost_page(self):
        """ Test to get the right template for the view """
        response = self.client.get('/popular_post/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'popular_post.html', 'base.html')

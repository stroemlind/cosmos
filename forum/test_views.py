from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post


# Create your tests here.
class TestViews(TestCase):
    """ Test the code for the views """
    def test_get_home_page(self):
        """ Test to get the right template for the view """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forum/index.html')

    def test_get_get_post_page(self):
        """ Test to get the right template for the view """
        post = Post.objects.create(name='Test Forum Post')
        response = self.client.get(f'/post/{post.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forum/post_detail.html')

    def test_get_category_page_page(self):
        """ Test to get the right template for the view """
        response = self.client.get('/category/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forum/category.html')

    def test_get_add_post_page(self):
        """ Test to get the right template for the view """
        response = self.client.get('/add_post/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forum/add_post.html')

    def test_get_add_comment_page(self):
        """ Test to get the right template for the view """
        post = Post.objects.create(name='Test Forum Post')
        response = self.client.get(f'/post/{post.id}/add_comment/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forum/add_comment.html')

    def test_get_editpost_page(self):
        """ Test to get the right template for the view """
        post = Post.objets.create(name='Test Forum Post')
        response = self.client.get(f'/post/edit/{post.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forum/edit_post.html')

    def test_get_deletepost_page(self):
        """ Test to get the right template for the view """
        post = Post.objects.create(name='Test Forum Post')
        response = self.client.get(f'/post/{post.id}/delete')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forum/delete_post.html')

    def test_get_like_view(self):
        """ Test to get the right template for the view """
        post = Post.objects.create(name='Test Forum Post')
        response = self.client.get(reverse(f'/like/{post.id}'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forum/post_detail.html')

    def test_get_mostlikedpost_page(self):
        """ Test to get the right template for the view """
        response = self.client.get('/popular_post/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forum/popular_post.html')


class TestUserOnlyFunctions(TestCase):
    """ Test for the views only accessable by Users """
    def setUp(self):
        # Create test users
        test_user1 = User.objects.create_user(
            username='testuser1',
            password='3E!uhGre09Wq'
            )

        test_user1.save()

    def test_can_add_post(self):
        """
        Test to see that that only a User,
        whos login in can do the following
        """
        login = self.clicent.login(
            username='testuser1',
            password='3E!uhGre09Wq'
            )
        # post = Post.objects.create(name='Test Forum Post')
        response = self.client.post(
            '/add_post/',
            {'title':'Test Added Post'}
            )
        self.assertRedirects(response, 'post/<int:pk>')  # f string here to get it right?

    def test_can_add_comment(self):
        """
        Test to see that that only a User,
        whos login in can do the following
        """
        login = self.clicent.login(
            username='testuser1',
            password='3E!uhGre09Wq'
            )
        post = Post.objects.create(name='Test Forum Post')
        response = self.client.post(
            f'/post/{post.id}/add_comment/',
            {'body': 'Test Added Comment'}
            )
        self.assertRedirects(response, f'/post/{post.id}')

    def test_can_edit_post(self):
        """
        Test to see that that only a User,
        whos login in can do the following
        """
        login = self.clicent.login(
            username='testuser1',
            password='3E!uhGre09Wq'
            )
        post = Post.objects.create(name='Test Forum Post')
        response = self.client.get(f'/post/edit/{post.id}')
        self.assertRedirects(response, '/')

    def test_can_delete_post(self):
        """
        Test to see that that only a User,
        whos login in can do the following
        """
        login = self.clicent.login(
            username='testuser1',
            password='3E!uhGre09Wq'
            )
        post = Post.objects.create(name='Test Forum Post')
        response = self.client.get(f'/post/{post.id}/delete')
        self.assertRedirects(response, '/')
        existing_posts = Post.objects.filter(id=post.id)
        self.assertEqual(len(existing_posts), 0)

    def test_can_like_post(self):
        """
        Test to see that that only a User,
        whos login in can do the following
        """
        login = self.clicent.login(
            username='testuser1',
            password='3E!uhGre09Wq'
            )
        post = Post.objects.create(name='Test Forum Post', liked=True)
        response = self.client.get(reverse(f'/like/{post.id}'))
        self.assertRedirects(response, f'/post/{post.id}')
        liked = Post.objects.get(id=post.id)
        self.assertFalse(liked.done)

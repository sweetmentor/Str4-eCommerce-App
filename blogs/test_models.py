from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User

class TestBlogModel(TestCase):

    def test_create_post(self):
        post = Post(content='Some test content.')
        post.save()
        self.assertEqual(post.content, "Some test content.")
        self.assertFalse(post.title)
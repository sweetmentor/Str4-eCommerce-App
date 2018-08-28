from django.apps import apps
from django.test import TestCase
from .apps import BlogsConfig


class TestblogConfig(TestCase):

    def test_blogs_app(self):
        self.assertEqual("blogs", BlogsConfig.name)
        self.assertEqual("blogs", apps.get_app_config("blogs").name)

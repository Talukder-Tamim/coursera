from django.test import SimpleTestCase
from django.urls import reverse, resolve
from coursera.views import create_course, all_course


class TestUrls(SimpleTestCase):

    def test_list_url_is_resolved(self):
        url = reverse('create-course')
        print(resolve(url))
        self.assertEqual(resolve(url).func, create_course)


    def test_list_url_is_resolved(self):
        url = reverse('course-list')
        print(resolve(url))
        self.assertEqual(resolve(url).func, all_course)
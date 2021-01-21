from django.test import SimpleTestCase
from django.urls import reverse, resolve
from coursera.views import create_course, all_course


class TestUrls(SimpleTestCase):

    def test_create_url_is_resolved(self):
        url = reverse('create-course')
        print(resolve(url))
        

    def test_list_url_is_resolved(self):
        url = reverse('course-list')
        print(resolve(url))


    def test_signup_url_is_resolved(self):
        url = reverse('signup')
        print(resolve(url))


    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        print(resolve(url))


    
        
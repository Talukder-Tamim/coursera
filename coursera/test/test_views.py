from django.test import TestCase, Client
from django.urls import reverse
from coursera.models import Courses, Student, Teacher
import json
from coursera.views import teacher_list, all_course



class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.course_url = reverse('all-course')
        self.login_url = reverse('login')
        self.enroll_course_url = reverse('course-list')


    def test_project_list_get(self):

        response = self.client.get(self.course_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'all_course.html')


    def test_project_login_get(self):
        response = self.client.get(self.login_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')


    def test_project_enroll_get(self):
        response = self.client.get(self.enroll_course_url)

        self.assernEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'course_list.html')





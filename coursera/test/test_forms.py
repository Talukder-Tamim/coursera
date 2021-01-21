from django.test import SimpleTestCase
from coursera.forms import CourseForm, TeacherForm
import unittest


class TestForm(SimpleTestCase):

    def test_form_course_is_valid(self):
        form = CourseForm(data={
            'title': 'web development',
            'duration': '2 months'
        })

        self.assertTrue(form.is_valid())


    def test_form_course_is_not_valid(self):
        form = CourseForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)


    def test_form_teacher_is_valid(self):
        form = TeacherForm(data={
            'first_name': 'Tamim',
            'last_name': 'Talukder',
            'email': 'a@gmail.com',
        })

        self.assertFalse(form.is_valid())


    def test_form_teacher_is_not_valid(self):
        form = TeacherForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 4)

    

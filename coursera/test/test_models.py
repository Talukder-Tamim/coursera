from django.test import TestCase
from django.contrib.auth.models import User
from coursera.models import Courses, Teacher, Student, Management


class TestModel(TestCase):

    def setUp(self):
        self.course1 = Courses.objects.create(
            title = 'django',
            duration = '2 months'
        )
        self.user1 = User.objects.create(
                username='Tamim'
            )
        self.student1 = Student.objects.create(
            user = self.user1,
            phone=123
        )
        self.teacher1 = Teacher.objects.create(
            user = self.user1,
            first_name='Atik'
        )
        self.staff1 = Management.objects.create(
            name = 'Asif',
            address = 'Dhaka'
        )

        
        
    def test_project_course(self):
        self.assertEqual(self.course1.title, 'django')
        self.assertEqual(self.course1.duration, '2 months')


    def test_project_student(self):
        self.assertEqual(self.student1.user.username, 'Tamim')
        self.assertEqual(self.student1.phone, 123)


    def test_project_teacher(self):
        self.assertEqual(self.teacher1.user.username, 'Tamim')
        self.assertEqual(self.teacher1.first_name, 'Atik')


    def test_project_management(self):
        self.assertEqual(self.staff1.name, 'Asif')
        self.assertEqual(self.staff1.address, 'Dhaka')
        
        
    
    

    


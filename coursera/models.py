from django.db import models
from django.contrib.auth.models import User


class Courses(models.Model):
    title = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title


class Student(models.Model):
    user = models.OneToOneField(User, related_name='student', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.IntegerField(blank=True, null=True)
    course = models.ManyToManyField(Courses, blank=True, null=True)


    def __str__(self):
        return self.first_name


class Teacher(models.Model):
    user = models.ForeignKey(User, related_name='teacher', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name


class Management(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name






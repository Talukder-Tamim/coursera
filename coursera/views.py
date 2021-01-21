from django.shortcuts import render, redirect
from .models import Courses, Teacher, Student
from .forms import CourseForm, TeacherForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import AnonymousUser

def create_course(request):
    if request.method == "POST":
        forms = CourseForm(request.POST)
        if forms.is_valid():
            course_title = forms.cleaned_data['title']
            course_duration = forms.cleaned_data['duration']
            course_description = forms.cleaned_data['description']

            Courses.objects.create(title=course_title, duration=course_duration, description=course_description)

            return redirect('all-course')
    else:
        forms = CourseForm()
        context = {'forms': forms}
        return render(request, 'create_course.html', context)  


def all_course(request):
    courses = Courses.objects.all()
    context = {'courses': courses}
    return render(request, 'all_course.html', context)


def teacher_list(request):
    teachers = Teacher.objects.all()
    context = {'teachers': teachers}
    return render(request, 'teacher_list.html', context)


def enroll_course(request):
    if request.method == "POST":
        course_id = request.POST['course']
        user_obj = request.user
        users = Student.objects.get(user=user_obj)   
        
        users.course.add(Courses.objects.get(id=course_id))

    users_obj = Student.objects.get(user=request.user)
    courses = Courses.objects.all()
    context = {'courses': courses, 'user_obj': users_obj}
    return render(request, 'course_list.html', context)


def signup(request):
    if request.method == "POST":
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        phone = request.POST['phone']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        radio_value = request.POST['user']

        if password1 == password2:
            if User.objects.filter(username=email).exists():
                messages.info(request, 'Email exists..')
                return render(request, 'signup.html')
            else:
                user = User.objects.create_user(username=email, password=password1)
                if radio_value == 'student':
                    student = Student()
                    student.user = user
                    student.first_name = first_name
                    student.last_name = last_name
                    student.phone = phone
                    student.save()
                    return redirect('login')

                if radio_value == 'teacher':
                    teacher = Teacher()
                    teacher.user = user
                    teacher.first_name = first_name
                    teacher.last_name = last_name
                    teacher.phone = phone
                    teacher.save()
                    return redirect('login')          
        else:
            messages.info(request, 'Password not matched..')
            return render(request, 'signup.html')
    else:
        return render(request, 'signup.html')


def user_login(request):
    if request.method=="POST":
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(username=email, password=password)

        if user is not None:
            login(request, user)
            try:
                if Student.objects.get(user__username=email):
                    return redirect('course-list')
                else:
                    messages.info(request, 'Username or password incorrect')
                    return render(request, 'login.html')
            except:
                if Teacher.objects.get(user__username=email):
                    return redirect('all-course')
                else:
                    messages.info(request, 'Username or password incorrect')
                    return render(request, 'login.html')
        else:
            messages.info(request, 'Username or password incorrect')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')



def user_logout(request):
    logout(request)
    return redirect('login')







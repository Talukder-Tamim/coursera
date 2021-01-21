from django.urls import path
from .import views


urlpatterns = [
    path('', views.user_login, name="login"),
    path('create/course', views.create_course, name="create-course"),
    path('course/list', views.enroll_course, name="course-list"),
    path('course/all', views.all_course, name="all-course"),
    path('teacher/list', views.teacher_list, name="teacher-list"),
    path('signup', views.signup, name="signup"),
    path('logout', views.user_logout, name="logout"),
    
]

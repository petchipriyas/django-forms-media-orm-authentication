from django.urls import path
from .views import MyView
from django.urls import path

from .views import (
    home,
    student_form,
    student_create,
    student_list,
    students_by_course,
    register,
    UserLoginView,
    UserLogoutView
)


urlpatterns = [

    path('', home, name='home'),

    path(
        'form/',
        student_form,
        name='student_form'
    ),

    path(
        'students/create/',
        student_create,
        name='student_create'
    ),

    path(
        'students/',
        student_list,
        name='student_list'
    ),

    path(
        'course/<int:course_id>/',
        students_by_course,
        name='students_by_course'
    ),

    path(
        'register/',
        register,
        name='register'
    ),

    path(
        'login/',
        UserLoginView.as_view(),
        name='login'
    ),

    path(
        'logout/',
        UserLogoutView.as_view(),
        name='logout'
    ),
]

#rlpatterns = [
   # path('student/', views.student_form, name='student_form'),
   # path('success/', views.success, name='success'),
    path('myview/', MyView.as_view()),
#]

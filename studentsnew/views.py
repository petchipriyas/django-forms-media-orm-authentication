from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from django.shortcuts import render, redirect
from .forms import StudentForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.db.models import Count

from .forms import StudentForm, StudentModelForm, RegisterForm
from .models import Student, Course


def home(request):
    return render(request, 'base.html')


# Normal Form
def student_form(request):

    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']

            return render(
                request,
                'student_form.html',
                {
                    'form': form,
                    'message': 'Form submitted successfully!'
                }
            )

    else:
        form = StudentForm()

    return render(
        request,
        'student_form.html',
        {'form': form}
    )


# ModelForm
@login_required
def student_create(request):

    if request.method == 'POST':

        form = StudentModelForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            form.save()
            return redirect('student_list')

    else:
        form = StudentModelForm()

    return render(
        request,
        'student_form.html',
        {'form': form}
    )


# Student List + ORM
@login_required
def student_list(request):

    students = Student.objects.all().order_by('name')

    older_students = Student.objects.filter(
        age__gt=20
    )

    excluded_students = Student.objects.exclude(
        age__lte=18
    )

    courses = Course.objects.annotate(
        student_count=Count('students')
    )

    return render(
        request,
        'student_list.html',
        {
            'students': students,
            'older_students': older_students,
            'excluded_students': excluded_students,
            'courses': courses
        }
    )


# Filter by Course
def students_by_course(request, course_id):

    students = Student.objects.filter(
        course_id=course_id
    )

    return render(
        request,
        'student_list.html',
        {
            'students': students
        }
    )


# Register
def register(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            user.set_password(
                form.cleaned_data['password']
            )

            user.save()

            login(request, user)

            return redirect('student_create')

    else:
        form = RegisterForm()

    return render(
        request,
        'register.html',
        {'form': form}
    )


# Login
class UserLoginView(LoginView):

    template_name = 'login.html'


# Logout
class UserLogoutView(LogoutView):

    pass


def student_form(request):

    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']

            print(name, email, age)

            return redirect('success')

    else:
        form = StudentForm()

    return render(request, 'student_form.html', {'form': form})


def success(request):
    return render(request, 'success.html')







class MyView(View):
    def get(self,request):
        return HttpResponse("this is aget request")




 
  #class TaskView(ListView):
   # model=Task
    #template_name=




from django.db import models

# Create your models here.
from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    profile_image = models.ImageField(
        upload_to='student_profiles/',
        blank=True,
        null=True
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='students'
    )

    def __str__(self):
        return self.name



class Task(models.Model):
    name=models.CharField(max_length=100)
    completed=models.BooleanField(default=True)

        def __str__(self):
            return self.name






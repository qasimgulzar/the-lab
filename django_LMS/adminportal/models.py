from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User


# Create your models here.
class Course(models.Model):
    course_code = models.CharField(max_length=10, default='')
    course_name = models.CharField(max_length=200)
    course_image = models.ImageField(default='django_LMS/static/adminportal/default.png')
    course_about_info = models.TextField(default="Course info")
    course_learning_oucomes = models.TextField(default="Course learning outcomes")
    instructor_image = models.ImageField(default = "django_LMS/static/adminportal/instructor.png")
    instructor_name = models.CharField(max_length=200, default="Instructor Name")
    instructor_designation = models.CharField(max_length=100,default="Instructor Designation")
    users_registered = models.ManyToManyField(User)


    def __str__(self):
        return self.course_name
        
admin.site.register(Course)
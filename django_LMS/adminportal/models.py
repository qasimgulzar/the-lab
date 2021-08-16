from django.db import models


# Create your models here.
class Course(models.Model):
    course_code = models.CharField(max_length=10, default='')
    course_name = models.CharField(max_length=200)

    def __str__(self):
        return self.course_name

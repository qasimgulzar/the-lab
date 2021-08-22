from http.client import HTTPResponse

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from .models import Course
from .serializers import CourseSerializer


# Create your views here.

class ListCourseAPIView(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CreateCourseAPIView(CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class UpdateCourseAPIView(UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class DeleteCourseAPIView(DestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


def index(request):
    return HttpResponse("course page")


def list_course_view(request):
    all_courses = Course.objects.all()
    context = {'list_of_courses': all_courses}
    return render(request, 'adminportal/course.html', context)

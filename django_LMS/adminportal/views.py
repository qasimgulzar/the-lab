from django.http import HttpResponse, request
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from adminportal.models import Course
from adminportal.serializers import CourseSerializer
from django.contrib import messages
from .forms import NewUserForm
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import AuthenticationForm
from time import sleep
from django.contrib.auth.models import User




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


def single_course_view(request, id):
    course = Course.objects.get(pk=id)
    current_user = request.user
    if current_user.id is not None:
        context = {'course': course,
                'isEnrolled': current_user in User.objects.filter(course__id = course.id)
                }
    else:
        context = {'course': course}
    return render(request, 'adminportal/single_course.html', context)


def list_course_view(request):
    all_courses = Course.objects.all()
    context = {'list_of_courses': all_courses}
    return render(request, 'adminportal/course.html', context)


def register_course(request, id):
    current_user = request.user
    if current_user.id is not None:
        course = Course.objects.get(pk = id)
        user = User.objects.get(pk = current_user.id)
        if user not in User.objects.filter(course__id = course.id):
            course.users_registered.add(user)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    else:
        	return redirect("login_request")

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are logged in as {username}.")
                return redirect("adminportal:all_courses")
            else:
                messages.error(request, "Invalid username or password!!")
        else:
            messages.error(request, "Invalid credentials!!")
    form = AuthenticationForm()
    return render(request=request, template_name="adminportal/login.html", context={"login_form": form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("login_request")


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        print("before balod", form.is_valid())
        if form.is_valid():
            print("sdakjgk")
            user = form.save()
            login(request, user)
            messages.success(request, "Registration Successful")
            return redirect("adminportal:all_courses")
        messages.error(request, 'Unsuccessful registration, Invalid Form')
    form = NewUserForm()
    return render(request=request, template_name="adminportal/register.html", context={"register_form": form})

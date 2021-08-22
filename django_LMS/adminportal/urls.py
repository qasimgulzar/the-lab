from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', views.list_course_view, name='index'),
                  path('course/', views.list_course_view, name='single_course_view'),
                  path('create/', views.CreateCourseAPIView.as_view(), name='create_course'),
                  path('update/<int:pk>/', views.UpdateCourseAPIView.as_view(), name='update_course'),
                  path('delete/<int:pk>/', views.DeleteCourseAPIView.as_view(), name='delete_course')
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

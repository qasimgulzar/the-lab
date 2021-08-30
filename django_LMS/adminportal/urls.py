from django.urls import path
from . import views
from django.urls import include

from django.conf import settings
from django.conf.urls.static import static

app_name = "adminportal"
urlpatterns = [
                  path('courses/', include('adminportal.courses_url'), name='all_courses'),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

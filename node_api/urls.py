from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [

    path('getAllStudents/', GetAllStudents.as_view(), name='getAllStudents'),
    path('getStudentByRollNo/', GetStudentByRollNo.as_view(), name='getStudentByRollNo'),
    path('getStudentsByDept/', GetStudentsByDept.as_view(), name='getStudentsByDept'),
    path('getStudentProfile/', GetStudentProfile.as_view(), name='getStudentProfile'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

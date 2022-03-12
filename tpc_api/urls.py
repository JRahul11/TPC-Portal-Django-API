from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from .views import *

urlpatterns = [
    path('addStudent/', addStudent, name='addStudent'),
    path('addAcademicInfo/', addAcademicInfo, name='addAcademicInfo'),
    path('addSkillSet/', addSkillSet, name='addSkillSet'),
    path('addExperience/', addExperience, name='addExperience'),
    path('addPlacementDetails/', addPlacementDetails, name='addPlacementDetails'),
    path('addOtherInfo/', addOtherInfo, name='addOtherInfo'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

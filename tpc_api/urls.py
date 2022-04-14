from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from rest_framework_simplejwt.views import (TokenRefreshView)
from .views import *

urlpatterns = [
    # Base URL
    path('', Welcome.as_view(), name='welcome'),

    # Insert/ Update
    path('addStudent/', AddStudent.as_view(), name='addStudent'),
    path('addAcademicInfo/', AddAcademicInfo.as_view(), name='addAcademicInfo'),
    path('addSkillSet/', AddSkillSet.as_view(), name='addSkillSet'),
    path('addExperience/', AddExperience.as_view(), name='addExperience'),
    path('addPlacementDetails/', AddPlacementDetails.as_view(), name='addPlacementDetails'),
    path('addOtherInfo/', AddOtherInfo.as_view(), name='addOtherInfo'),

    # Retrieve
    path('viewStudent/', ViewStudent.as_view(), name='viewStudent'),
    path('viewAcademicInfo/', ViewAcademicInfo.as_view(), name='viewAcademicInfo'),
    path('viewSkillSet/', ViewSkillSet.as_view(), name='viewSkillSet'),
    path('viewExperience/', ViewExperience.as_view(), name='viewExperience'),
    path('viewPlacementDetails/', ViewPlacementDetails.as_view(), name='viewPlacement'),
    path('viewOtherInfo/', ViewOtherInfo.as_view(), name='viewOtherInfo'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

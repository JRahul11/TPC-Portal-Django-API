from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    # Base URL
    path('', Welcome.as_view()),

    # Insert/ Update
    path('addStudent/', AddStudent.as_view()),
    path('addAcademicInfo/', AddAcademicInfo.as_view()),
    path('addSkillSet/', AddSkillSet.as_view()),
    path('addExperience/', AddExperience.as_view()),
    path('addPlacementDetails/', AddPlacementDetails.as_view()),
    path('addOtherInfo/', AddOtherInfo.as_view()),

    # Retrieve
    path('viewStudent/', ViewStudent.as_view()),
    path('viewAcademicInfo/', ViewAcademicInfo.as_view()),
    path('viewSkillSet/', ViewSkillSet.as_view()),
    path('viewExperience/', ViewExperience.as_view()),
    path('viewPlacementDetails/', ViewPlacementDetails.as_view()),
    path('viewOtherInfo/', ViewOtherInfo.as_view()),
    
    # Notifications
    path('notifications/', Notifications.as_view()),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [

    path('addBatchViaExcel/', AddBatchViaExcel.as_view()),
    
    path('addPlacedStudents/', AddPlacedStudents.as_view())

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

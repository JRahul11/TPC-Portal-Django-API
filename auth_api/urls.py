from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from rest_framework_simplejwt.views import (TokenRefreshView)
from .views import *

urlpatterns = [

    path('studentLogin/', StudentLogin.as_view(), name='studentLogin'),
    path('studentLogin/tokenRefresh/', TokenRefreshView.as_view()),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

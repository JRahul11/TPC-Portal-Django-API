from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # Admin Panel URL
    path('admin/', admin.site.urls),
    
    # Auth URLs
    path('auth/', include('auth_api.urls')),

    # Django URLs
    path('', include('tpc_api.urls')),

    # NodeJS URLS
    path('node/', include('node_api.urls')),
    
    # Admin URLs
    path('superuser/', include('superuser.urls')),
    
    # Company URLs
    path('company/', include('company.urls'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bulgaria_trips.web.urls')),
    path('accounts/', include('bulgaria_trips.accounts.urls')),
    path('mountain/', include('bulgaria_trips.mountain.urls')),
    path('beaches/', include('bulgaria_trips.beaches.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


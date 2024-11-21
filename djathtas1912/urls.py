from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    path('djathtas1912-admin//defender/', include('defender.urls')),
    path('djathtas1912-admin/', admin.site.urls),
    path('',include("djathtasApp.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
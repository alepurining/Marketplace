from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Marketplace.views import listatecnicos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tecnicos/', listatecnicos, name='listatecnicos'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

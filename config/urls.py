from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Marketplace import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.listacategorias, name='inicio'),

    # Categorías
    path('categorias/', views.listacategorias, name='listacategorias'),
    path('categorias/<int:pk>/', views.detalle_categoria, name='detalle_categoria'),

    # Técnicos
    path('tecnicos/', views.listatecnicos, name='listatecnicos'),
    path('tecnicos/<int:pk>/', views.detalle_tecnico, name='detalle_tecnico'),

    # Clientes
    path('clientes/', views.listaclientes, name='listaclientes'),
    path('clientes/<int:pk>/', views.detalle_cliente, name='detalle_cliente'),

    # Solicitudes
    path('solicitudes/', views.listasolicitudes, name='listasolicitudes'),
    path('solicitudes/<int:pk>/', views.detalle_solicitud, name='detalle_solicitud'),

    # Pagos
    path('pagos/', views.listapagos, name='listapagos'),
    path('pagos/<int:pk>/', views.detalle_pago, name='detalle_pago'),

    # Calificaciones
    path('calificaciones/', views.listacalificaciones, name='listacalificaciones'),
    path('calificaciones/<int:pk>/', views.detalle_calificacion, name='detalle_calificacion'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
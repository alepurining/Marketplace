from django.contrib import admin

# Register your models here.

from .models import (
    CategoriaServicio,
    Tecnico,
    Cliente,
    SolicitudServicio,
    Pago,
    Calificacion
)

admin.site.register(CategoriaServicio)
admin.site.register(Tecnico)
admin.site.register(Cliente)
admin.site.register(SolicitudServicio)
admin.site.register(Pago)
admin.site.register(Calificacion)
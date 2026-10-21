from django.db import models

# Create your models here.
class CategoriaServicio(models.Model):
    categoria_id = models.CharField(max_length=10, primary_key = True) 
    categoria_name = models.CharField(max_length=50) 
    categoria_description = models.TextField() 

    def __str__(self): 
        return self.categoria_id
    
#--------------------------------------------------------------------------------

class Proveedor(models.Model): 
    proveedor_id = models.CharField(max_length=5, primary_key=True) 
    proveedor_name_completo = models.CharField(max_length=200) 
    proveedor_telefono = models.CharField(max_length=15)
    proveedor_email = models.EmailField(null = True)
    proveedor_tarifa_por_hora = models.DecimalField(max_digits=10, decimal_places=2)
    proveedor_experiencia_anos = models.PositiveIntegerField()
    proveedor_disponible = models.BooleanField(default=True)

    categoria = models.ForeignKey(CategoriaServicio, on_delete=models.CASCADE) 

    def __str__(self): 
            return self.proveedor_id

#--------------------------------------------------------------------------------

class Cliente(models.Model): 
    cliente_id = models.CharField(max_length=5, primary_key=True) 
    cliente_name_completo = models.CharField(max_length=200) 
    cliente_telefono = models.CharField(max_length=15)
    cliente_email = models.EmailField(null = True)
    cliente_direccion_principal = models.CharField(max_length=200)

    def __str__(self): 
        return self.cliente_id

#--------------------------------------------------------------------------------

class SolicitudServicio(models.Model): 
    solicitud_id = models.CharField(max_length=5, primary_key=True) 
    solicitud_direccion_trabajo = models.CharField(max_length=200) 
    solicitud_descripcion_trabajo = models.TextField()
    solicitud_fecha_programada = models.DateField()
    estado = models.CharField(max_length=20, default='pendiente')
    solicitud_creado_el = models.DateTimeField(auto_now_add=True)

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

    def __str__(self):  
        return self.solicitud_id

#--------------------------------------------------------------------------------


class Pago(models.Model):
    pago_id = models.CharField(max_length=10, primary_key=True)
    pago_monto = models.DecimalField(max_digits=10, decimal_places=2)
    pago_metodo_pago = models.CharField(max_length=20)
    pago_pagado = models.BooleanField(default=False)
    pago_fecha_pago = models.DateTimeField(auto_now_add=True)

    solicitud = models.ForeignKey(SolicitudServicio, on_delete=models.CASCADE)

    def __str__(self):
        return self.pago_id

#--------------------------------------------------------------------------------

class Calificacion(models.Model):
    calificacion_id = models.CharField(max_length=10, primary_key=True)
    calificacion_puntuacion = models.PositiveIntegerField()
    calificacion_comentario = models.TextField()
    calificacion_fecha = models.DateTimeField(auto_now_add=True)

    solicitud = models.ForeignKey(SolicitudServicio, on_delete=models.CASCADE)

    def __str__(self):
        return self.calificacion_id

     
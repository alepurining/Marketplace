from django import forms
from Marketplace.models import CategoriaServicio, Tecnico, Cliente, SolicitudServicio, Pago, Calificacion


# --------------------------------------------------------------------------------
class CategoriaServicioForm(forms.ModelForm):
    class Meta:
        model = CategoriaServicio
        fields = ['categoria_name', 'categoria_description', 'categoria_image']


# ----------------------------------------
class CalificacionForm(forms.ModelForm):
    class Meta:
        model = Calificacion
        fields = '__all__'
        widgets = {
            'calificacion_puntuacion': forms.Select(choices=[
                (1, '1 - Muy malo'),
                (2, '2 - Malo'),
                (3, '3 - Regular'),
                (4, '4 - Bueno'),
                (5, '5 - Excelente'),
            ]),
        }


# ----------------------------------------
class ClientesForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'


# ----------------------------------------
class PagosForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = '__all__'
        widgets = {
            'pago_estado_pago': forms.Select(choices=[
                (False, 'Pendiente'),
                (True, 'Pagado'),
            ]),
        }


# ----------------------------------------
class TecnicoForm(forms.ModelForm):
    class Meta:
        model = Tecnico
        fields = '__all__'
        widgets = {
            'tecnico_estado': forms.Select(choices=[
                (False, 'Inactivo'),
                (True, 'Activo'),
            ]),
        }


# ----------------------------------------
class SolicitudServicioForm(forms.ModelForm):
    class Meta:
        model = SolicitudServicio
        fields = '__all__'
        widgets = {
            'solicitud_fecha_programada': forms.DateInput(attrs={
                'type': 'date',
            }),
        
            'estado': forms.Select(choices=[
                    ('pendiente', 'Pendiente'),
                    ('en_proceso', 'En proceso'),
                    ('completada', 'Completada'),
                    ('cancelada', 'Cancelada'),
            ]),
        }
# ----------------------------------------
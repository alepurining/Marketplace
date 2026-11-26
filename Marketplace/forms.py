from django import forms
from Marketplace.models import CategoriaServicio, Tecnico, Cliente, SolicitudServicio, Pago, Calificacion

class CategoriaServicioForm(forms.ModelForm):
    
    class Meta:
        model = CategoriaServicio
        fields = ['categoria_name', 'categoria_description', 'categoria_image']
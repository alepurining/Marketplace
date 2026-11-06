from django.shortcuts import render
from Marketplace.models import Tecnico

# Create your views here.
def listatecnicos(request):
    tecnicos = Tecnico.objects.all() # select * from tecnico
    return render(request, 'tecnicos/lista_de_tecnicos.html', 
                  {'tecnicos': tecnicos})
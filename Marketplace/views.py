from django.shortcuts import render, get_object_or_404, redirect
from .models import CategoriaServicio, Tecnico, Cliente, SolicitudServicio, Pago, Calificacion
from .forms import CategoriaServicioForm

# --- CATEGORÍAS DE SERVICIO ---
def listacategorias(request):
    categorias = CategoriaServicio.objects.all()
    return render(request, 'categoriasservicio/lista_categoriasservicios.html', {'categorias': categorias})

def detalle_categoria(request, pk):
    categoria = get_object_or_404(CategoriaServicio, pk=pk)
    return render(request, 'categoriasservicio/detalle_categoriasservicio.html', {'categoria': categoria})

# Registrar Categoría de Servicio
def registrar_categoria(request):

    if request.method == 'POST':
        form = CategoriaServicioForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('listacategorias')
    else:
        form = CategoriaServicioForm()
    return render(request, 'categoriasservicio/formulario_categoria.html', {'form': form})

# --- TÉCNICOS ---
def listatecnicos(request):
    tecnicos = Tecnico.objects.all()
    return render(request, 'tecnicos/lista_de_tecnicos.html', {'tecnicos': tecnicos})

def detalle_tecnico(request, pk):
    tecnico = get_object_or_404(Tecnico, pk=pk)
    return render(request, 'tecnicos/detalle_tecnico.html', {'tecnico': tecnico})


# --- CLIENTES ---
def listaclientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})

def detalle_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    return render(request, 'clientes/detalle_cliente.html', {'cliente': cliente})


# --- SOLICITUDES DE SERVICIO ---
def listasolicitudes(request):
    solicitudes = SolicitudServicio.objects.all()
    return render(request, 'solicitudes/lista_solicitudes.html', {'solicitudes': solicitudes})


# --- PAGOS ---
def listapagos(request):
    pagos = Pago.objects.all()
    return render(request, 'pagos/lista_pagos.html', {'pagos': pagos})

def detalle_pago(request, pk):
    pago = get_object_or_404(Pago, pk=pk)
    return render(request, 'pagos/detalle_pagos.html', {'pago': pago})


# --- CALIFICACIONES ---
def listacalificaciones(request):
    calificaciones = Calificacion.objects.all()
    return render(request, 'calificaciones/lista_calificaciones.html', {'calificaciones': calificaciones})



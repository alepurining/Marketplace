# Marketplace de Servicios Técnicos

Este proyecto consiste en una plataforma web desarrollada con Django que conecta a profesionales e independientes técnicos (plomeros, electricistas, carpinteros, entre otros) con clientes que requieren reparaciones o mantenimiento local.

## Integrantes
* Yudy Mayorga

## Descripción y Funcionalidad
El sistema permite gestionar de manera integral la contratación de servicios técnicos mediante las siguientes funciones:

* Organizar los servicios por categorías especializadas.
* Administrar perfiles de proveedores con sus datos de contacto, tarifas e historial.
* Registrar clientes y agendar solicitudes de servicio.
* Llevar un control sobre el estado de cada solicitud y su pago correspondiente.
* Calificar y retroalimentar la calidad del trabajo recibido.


### Pasos de Instalación y Ejecución (Windows)

Abre la terminal de Windows en la carpeta del proyecto y ejecuta los siguientes bloques de comandos:

1. **Clonar el repositorio y entrar a la carpeta:**
  * git clone [https://github.com/alepurining/Marketplace.git](https://github.com/alepurining/Marketplace.git) && cd Marketplace

2. Crear el entorno virtual, activarlo e instalar dependencias:
  * python -m venv venv && venv\Scripts\activate && pip install -r requirements.txt

3. Aplicar migraciones e iniciar el servidor local:
  * python manage.py migrate && python manage.py runserver



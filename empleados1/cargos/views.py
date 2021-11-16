from django.shortcuts import render
from cargos.models import Empleado


def index(request):
    return render(request, "deportes/Index.html")


def empleados(request):
    ofi = request.GET['Oficio']
    emple = Empleado()
    cursor = emple.devolverdato(ofi)
    contexto = {
        'listado_empleados': cursor
    }
    return render(request, "deportes/Empleados.html", contexto)
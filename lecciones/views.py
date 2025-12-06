from rest_framework import viewsets
from django.shortcuts import render, get_object_or_404
from .models import Leccion
from .serializers import LeccionSerializer
from cursos.models import Modulo, Inscripcion

class LeccionViewSet(viewsets.ModelViewSet):
    queryset = Leccion.objects.all()
    serializer_class = LeccionSerializer


def lista_lecciones(request, modulo_id):
    modulo = get_object_or_404(Modulo, id=modulo_id)
    lecciones = Leccion.objects.filter(modulo=modulo)
    
    context = {
        'modulo': modulo,
        'lecciones': lecciones,
        'curso': modulo.curso,
    }
    return render(request, 'lecciones/lista_lecciones.html', context)


def detalle_leccion(request, leccion_id):
    leccion = get_object_or_404(Leccion, id=leccion_id)
    modulo = leccion.modulo
    
    context = {
        'leccion': leccion,
        'modulo': modulo,
        'curso': modulo.curso,
    }
    return render(request, 'lecciones/detalle_leccion.html', context)

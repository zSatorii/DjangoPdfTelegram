from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Tarea, EntregaTarea, Examen
from .serializers import TareaSerializer, EntregaTareaSerializer, ExamenSerializer

class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer


class EntregaTareaViewSet(viewsets.ModelViewSet):
    serializer_class = EntregaTareaSerializer
    
    def get_queryset(self):
        return EntregaTarea.objects.filter(estudiante__usuario=self.request.user)


class ExamenViewSet(viewsets.ModelViewSet):
    queryset = Examen.objects.all()
    serializer_class = ExamenSerializer


@login_required
def lista_tareas(request):
    entregas = EntregaTarea.objects.filter(estudiante__usuario=request.user)
    context = {'entregas': entregas}
    return render(request, 'evaluaciones/lista_tareas.html', context)


@login_required
def entregar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    estudiante = request.user.estudiante
    
    if request.method == 'POST':
        archivo = request.FILES.get('archivo')
        if archivo:
            EntregaTarea.objects.update_or_create(
                tarea=tarea,
                estudiante=estudiante,
                defaults={'archivo': archivo}
            )
            return redirect('lista_tareas')
    
    context = {'tarea': tarea}
    return render(request, 'evaluaciones/entregar_tarea.html', context)


def examen_detalle(request, examen_id):
    examen = get_object_or_404(Examen, id=examen_id)
    context = {'examen': examen}
    return render(request, 'evaluaciones/examen.html', context)


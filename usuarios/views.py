from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404
from .models import Estudiante, Instructor
from .serializers import EstudianteSerializer, InstructorSerializer

class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer
    
    @action(detail=False, methods=['get'])
    def mi_perfil(self, request):
        estudiante = get_object_or_404(Estudiante, usuario=request.user)
        serializer = self.get_serializer(estudiante)
        return Response(serializer.data)


class InstructorViewSet(viewsets.ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer
    
    @action(detail=False, methods=['get'])
    def mis_datos(self, request):
        instructor = get_object_or_404(Instructor, usuario=request.user)
        serializer = self.get_serializer(instructor)
        return Response(serializer.data)


def perfil_usuario(request):
    context = {}
    if hasattr(request.user, 'estudiante'):
        context['tipo_usuario'] = 'estudiante'
        context['perfil'] = request.user.estudiante
    elif hasattr(request.user, 'instructor'):
        context['tipo_usuario'] = 'instructor'
        context['perfil'] = request.user.instructor
    return render(request, 'usuarios/perfil.html', context)


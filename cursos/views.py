from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import render
from django.db.models import Q
from .models import Curso, Inscripcion, Certificado
from .serializers import CursoSerializer, InscripcionSerializer, CertificadoSerializer

class CursoViewSet(viewsets.ModelViewSet):
    serializer_class = CursoSerializer
    
    def get_queryset(self):
        return Curso.objects.filter(publicado=True)
    
    @action(detail=False, methods=['get'])
    def cursos_del_instructor(self, request):
        instructor = request.user.instructor
        cursos = Curso.objects.filter(instructor=instructor)
        serializer = self.get_serializer(cursos, many=True)
        return Response(serializer.data)


class InscripcionViewSet(viewsets.ModelViewSet):
    serializer_class = InscripcionSerializer
    
    def get_queryset(self):
        return Inscripcion.objects.filter(estudiante__usuario=self.request.user)


class CertificadoViewSet(viewsets.ModelViewSet):
    serializer_class = CertificadoSerializer
    
    def get_queryset(self):
        return Certificado.objects.filter(estudiante__usuario=self.request.user)


def lista_cursos(request):
    cursos = Curso.objects.filter(publicado=True)
    context = {'cursos': cursos}
    return render(request, 'cursos/lista_cursos.html', context)


def detalle_curso(request, pk):
    curso = Curso.objects.get(pk=pk)
    inscrito = Inscripcion.objects.filter(
        estudiante__usuario=request.user,
        curso=curso
    ).exists()
    context = {
        'curso': curso,
        'inscrito': inscrito,
    }
    return render(request, 'cursos/detalle_curso.html', context)

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q, Count
from django.core.mail import EmailMessage
from django.contrib import messages
from django.conf import settings

from .models import Curso, Inscripcion, Certificado, Estudiante
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

def enviar_certificado(request, curso_id):
    curso = Curso.objects.get(pk=curso_id)

    if request.method == "POST":
        email_destino = request.POST.get('email_destino')
        print("ENVIAR_CERTIFICADO A:", email_destino)

        asunto = f'Certificado del curso {curso.titulo}'
        cuerpo = 'Adjuntamos tu certificado del curso.'

        correo = EmailMessage(
            asunto,
            cuerpo,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[email_destino],
        )
        correo.send()

        messages.success(request, 'Certificado enviado correctamente.')
        return redirect('detalle_curso', pk=curso.id)

    return redirect('detalle_curso', pk=curso.id)

def inscribirse(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    estudiante = Estudiante.objects.get(usuario=request.user)
    Inscripcion.objects.get_or_create(estudiante=estudiante, curso=curso)
    return redirect('detalle_curso', pk=curso.id)

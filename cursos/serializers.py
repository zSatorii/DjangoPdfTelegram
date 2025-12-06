from rest_framework import serializers
from .models import Curso, Modulo, Inscripcion, Certificado
from usuarios.serializers import InstructorSerializer

class ModuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modulo
        fields = ['id', 'titulo', 'descripcion', 'orden']


class CursoSerializer(serializers.ModelSerializer):
    instructor = InstructorSerializer(read_only=True)
    modulos = ModuloSerializer(many=True, read_only=True)
    
    class Meta:
        model = Curso
        fields = [
            'id', 'titulo', 'descripcion', 'instructor', 'precio', 
            'nivel', 'duracion', 'fecha_creacion', 'publicado', 'imagen', 'modulos'
        ]


class InscripcionSerializer(serializers.ModelSerializer):
    curso = CursoSerializer(read_only=True)
    
    class Meta:
        model = Inscripcion
        fields = [
            'id', 'curso', 'fecha_inscripcion', 'completado', 
            'progreso', 'fecha_completado'
        ]


class CertificadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificado
        fields = [
            'id', 'curso', 'fecha_emision', 'codigo_verificacion', 'calificacion_final'
        ]


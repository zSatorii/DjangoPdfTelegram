from rest_framework import serializers
from .models import Estudiante, Instructor
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class EstudianteSerializer(serializers.ModelSerializer):
    usuario = UserSerializer(read_only=True)
    
    class Meta:
        model = Estudiante
        fields = [
            'id', 'usuario', 'fecha_nacimiento', 'telefono', 
            'pais', 'fecha_registro', 'nivel_educativo'
        ]


class InstructorSerializer(serializers.ModelSerializer):
    usuario = UserSerializer(read_only=True)
    
    class Meta:
        model = Instructor
        fields = [
            'id', 'usuario', 'especialidad', 'biografia', 
            'experiencia', 'sitio_web', 'calificacion_promedio'
        ]

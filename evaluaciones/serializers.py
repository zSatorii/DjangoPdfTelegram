from rest_framework import serializers
from .models import Tarea, EntregaTarea, Examen

class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = ['id', 'leccion', 'titulo', 'descripcion', 'fecha_limite', 'puntaje_maximo']


class EntregaTareaSerializer(serializers.ModelSerializer):
    tarea_titulo = serializers.CharField(source='tarea.titulo', read_only=True)
    
    class Meta:
        model = EntregaTarea
        fields = [
            'id', 'tarea', 'tarea_titulo', 'archivo', 'fecha_entrega',
            'calificacion', 'comentarios'
        ]


class ExamenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Examen
        fields = [
            'id', 'curso', 'titulo', 'descripcion', 'duracion',
            'intentos_permitidos', 'fecha_limite'
        ]

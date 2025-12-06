from rest_framework import serializers
from .models import Leccion

class LeccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leccion
        fields = [
            'id', 'modulo', 'titulo', 'tipo', 'contenido', 
            'duracion', 'orden', 'recursos'
        ]

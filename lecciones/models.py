from django.db import models
from cursos.models import Modulo

class Leccion(models.Model):
    TIPO_LECCION_CHOICES = [
        ('video', 'Video'),
        ('texto', 'Texto'),
        ('quiz', 'Quiz'),
        ('tarea', 'Tarea'),
    ]
    
    modulo = models.ForeignKey(Modulo, on_delete=models.CASCADE, related_name='lecciones')
    titulo = models.CharField(max_length=200)
    tipo = models.CharField(max_length=20, choices=TIPO_LECCION_CHOICES)
    contenido = models.TextField()
    duracion = models.IntegerField(help_text="Duración en minutos")
    orden = models.IntegerField()
    recursos = models.FileField(upload_to='recursos/', blank=True, null=True)
    
    class Meta:
        db_table = 'leccion'
        ordering = ['orden']
    
    def __str__(self):
        return f"{self.modulo.titulo} - {self.titulo}"

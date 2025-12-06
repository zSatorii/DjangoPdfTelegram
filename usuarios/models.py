from django.db import models
from django.contrib.auth.models import User

class Estudiante(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='estudiante')
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=15)
    pais = models.CharField(max_length=50)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    nivel_educativo = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'estudiante'
        verbose_name_plural = 'Estudiantes'
    
    def __str__(self):
        return f"{self.usuario.get_full_name()} - Estudiante"


class Instructor(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='instructor')
    especialidad = models.CharField(max_length=100)
    biografia = models.TextField()
    experiencia = models.IntegerField(help_text="Años de experiencia")
    sitio_web = models.URLField(blank=True, null=True)
    calificacion_promedio = models.DecimalField(
        max_digits=3, decimal_places=2, default=0
    )
    
    class Meta:
        db_table = 'instructor'
        verbose_name_plural = 'Instructores'
    
    def __str__(self):
        return f"{self.usuario.get_full_name()} - {self.especialidad}"

from django.db import models
from usuarios.models import Instructor, Estudiante

class Curso(models.Model):
    NIVEL_CHOICES = [
        ('principiante', 'Principiante'),
        ('intermedio', 'Intermedio'),
        ('avanzado', 'Avanzado'),
    ]
    
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name='cursos')
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    nivel = models.CharField(max_length=20, choices=NIVEL_CHOICES)
    duracion = models.IntegerField(help_text="Duración en horas")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    publicado = models.BooleanField(default=False)
    imagen = models.ImageField(upload_to='cursos/', null=True, blank=True)
    
    class Meta:
        db_table = 'curso'
        ordering = ['-fecha_creacion']
    
    def __str__(self):
        return self.titulo


class Modulo(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='modulos')
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    orden = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'modulo'
        ordering = ['orden']
    
    def __str__(self):
        return f"{self.curso.titulo} - {self.titulo}"


class Inscripcion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name='inscripciones')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='inscripciones')
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)
    completado = models.BooleanField(default=False)
    progreso = models.IntegerField(default=0)
    fecha_completado = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        db_table = 'inscripcion'
        unique_together = ('estudiante', 'curso')
    
    def __str__(self):
        return f"{self.estudiante.usuario.username} - {self.curso.titulo}"


class Certificado(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name='certificados')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='certificados')
    fecha_emision = models.DateTimeField(auto_now_add=True)
    codigo_verificacion = models.CharField(max_length=100, unique=True)
    calificacion_final = models.DecimalField(max_digits=5, decimal_places=2)
    
    class Meta:
        db_table = 'certificado'
    
    def __str__(self):
        return f"Certificado {self.codigo_verificacion}"

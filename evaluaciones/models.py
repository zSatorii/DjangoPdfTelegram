from django.db import models
from lecciones.models import Leccion
from cursos.models import Curso
from usuarios.models import Estudiante

class Tarea(models.Model):
    leccion = models.ForeignKey(Leccion, on_delete=models.CASCADE, related_name='tareas')
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_limite = models.DateTimeField()
    puntaje_maximo = models.IntegerField()
    
    class Meta:
        db_table = 'tarea'
    
    def __str__(self):
        return self.titulo


class EntregaTarea(models.Model):
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE, related_name='entregas')
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name='entregas_tareas')
    archivo = models.FileField(upload_to='entregas/')
    fecha_entrega = models.DateTimeField(auto_now_add=True)
    calificacion = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )
    comentarios = models.TextField(blank=True)
    
    class Meta:
        db_table = 'entrega_tarea'
        unique_together = ('tarea', 'estudiante')
    
    def __str__(self):
        return f"{self.tarea.titulo} - {self.estudiante.usuario.username}"


class Examen(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='examenes')
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    duracion = models.IntegerField(help_text="Duración en minutos")
    intentos_permitidos = models.IntegerField(default=1)
    fecha_limite = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        db_table = 'examen'
    
    def __str__(self):
        return self.titulo


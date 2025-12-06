from django.contrib import admin
from .models import Curso

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'nivel', 'instructor', 'fecha_creacion')
    list_filter = ('nivel', 'instructor')
    search_fields = ('titulo', 'descripcion')

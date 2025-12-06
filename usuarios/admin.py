from django.contrib import admin
from .models import Instructor

@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'especialidad')
    search_fields = ('usuario__username', 'usuario__first_name', 'usuario__last_name')

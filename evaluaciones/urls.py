from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    TareaViewSet, EntregaTareaViewSet, ExamenViewSet,
    lista_tareas, entregar_tarea, examen_detalle
)

router = DefaultRouter()
router.register(r'tareas', TareaViewSet)
router.register(r'entregas', EntregaTareaViewSet, basename='entrega')
router.register(r'examenes', ExamenViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('tareas/', lista_tareas, name='lista_tareas'),
    path('entregar/<int:tarea_id>/', entregar_tarea, name='entregar_tarea'),
    path('examen/<int:examen_id>/', examen_detalle, name='examen_detalle'),
]

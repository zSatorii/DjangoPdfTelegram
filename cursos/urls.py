from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CursoViewSet,
    InscripcionViewSet,
    CertificadoViewSet,
    lista_cursos,
    detalle_curso,
    enviar_certificado,   
)

router = DefaultRouter()
router.register(r'cursos', CursoViewSet, basename='curso')
router.register(r'inscripciones', InscripcionViewSet, basename='inscripcion')
router.register(r'certificados', CertificadoViewSet, basename='certificado')

urlpatterns = [
    path('api/', include(router.urls)),
    path('', lista_cursos, name='lista_cursos'),
    path('<int:pk>/', detalle_curso, name='detalle_curso'),
    path(
        'curso/<int:curso_id>/enviar-certificado/',
        enviar_certificado,
        name='enviar_certificado'
    ),
]

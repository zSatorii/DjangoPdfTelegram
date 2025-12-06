from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EstudianteViewSet, InstructorViewSet, perfil_usuario

router = DefaultRouter()
router.register(r'estudiantes', EstudianteViewSet)
router.register(r'instructores', InstructorViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('perfil/', perfil_usuario, name='perfil_usuario'),
]

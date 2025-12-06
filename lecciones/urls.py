from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LeccionViewSet, lista_lecciones, detalle_leccion

router = DefaultRouter()
router.register(r'lecciones', LeccionViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('modulo/<int:modulo_id>/', lista_lecciones, name='lista_lecciones'),
    path('<int:leccion_id>/', detalle_leccion, name='detalle_leccion'),
]

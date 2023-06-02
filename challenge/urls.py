
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from Core.views import EmpresaViewSet, ColaboradorViewSet, OrganogramaViewSet

router = routers.DefaultRouter()
router.register(r'empresas', EmpresaViewSet)
router.register(r'colaboradores', ColaboradorViewSet)
router.register(r'organogramas', OrganogramaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/<int:empresa_id>/colaboradores/', ColaboradorViewSet.as_view({'get': 'list_by_empresa'}), name='colaboradores-empresa'),
]

from django.contrib import admin
from rest_framework import routers
from django.urls import path, include
from aluno.views import UserViewSet, AlunoViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'alunos', AlunoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework'))
]

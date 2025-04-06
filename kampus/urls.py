from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from mahasiswa.views import MahasiswaViewSet

router = DefaultRouter()
router.register(r'mahasiswa', MahasiswaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
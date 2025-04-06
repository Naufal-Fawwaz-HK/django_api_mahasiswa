from rest_framework import viewsets
from .models import Mahasiswa
from .serializers import MahasiswaSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Mahasiswa

@api_view(['GET'])
def get_choices(request):
    return Response({
        'fakultas': dict(Mahasiswa.FAKULTAS_CHOICES),
        'jurusan': dict(Mahasiswa.JURUSAN_CHOICES),
        'prodi': dict(Mahasiswa.PRODI_CHOICES)
    })

class MahasiswaViewSet(viewsets.ModelViewSet):
    queryset = Mahasiswa.objects.all()
    serializer_class = MahasiswaSerializer
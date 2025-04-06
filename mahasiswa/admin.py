from django.contrib import admin
from .models import Mahasiswa

@admin.register(Mahasiswa)
class MahasiswaAdmin(admin.ModelAdmin):
    list_display = ('nama', 'nim', 'fakultas', 'jurusan', 'ipk')
    search_fields = ('nama', 'nim')
    list_filter = ('fakultas', 'jurusan')
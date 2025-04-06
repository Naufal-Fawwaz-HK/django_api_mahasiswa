from django.db import models

class Mahasiswa(models.Model):
    FAKULTAS_CHOICES = [
        ('FH', 'Fakultas Hukum'),
        ('FEB', 'Fakultas Ekonomi dan Bisnis'),
        ('FK', 'Fakultas Kedokteran'),
        ('FKG', 'Fakultas Kedokteran Gigi'),
        ('FTSP', 'Fakultas Teknik Sipil dan Perencanaan'),
        ('FTI', 'Fakultas Teknologi Industri'),
        ('FTKE', 'Fakultas Teknologi Kebumian dan Energi'),
        ('FALTL', 'Fakultas Arsitektur Lanskap dan Teknologi Lingkungan'),
        ('FSRD', 'Fakultas Seni Rupa dan Desain'),
    ]

    JURUSAN_CHOICES = [
        ('TI', 'Teknik Informatika'),
        ('SI', 'Sistem Informasi'),
        ('TE', 'Teknik Elektro'),
        ('TM', 'Teknik Mesin'),
        ('TInd', 'Teknik Industri'),
        ('TS', 'Teknik Sipil'),
        ('Ars', 'Arsitektur'),
        ('PWK', 'Perencanaan Wilayah dan Kota'),
        ('TG', 'Teknik Geologi'),
        ('TPM', 'Teknik Perminyakan'),
        ('TPT', 'Teknik Pertambangan'),
        ('DI', 'Desain Interior'),
        ('DP', 'Desain Produk'),
        ('DKV', 'Desain Komunikasi Visual'),
        ('AL', 'Arsitektur Lanskap'),
        ('TL', 'Teknik Lingkungan'),
        ('Man', 'Manajemen'),
        ('Ak', 'Akuntansi Perpajakan'),
        ('EP', 'Ekonomi Pembangunan'),
        ('Hukum', 'Ilmu Hukum'),
        ('Kedokteran', 'Pendidikan Dokter'),
        ('KedokteranGigi', 'Pendidikan Dokter Gigi'),
    ]
    
    PRODI_CHOICES = [
        ('S1TI', 'S1 Informatika'),
        ('S1SI', 'S1 Sistem Informasi'),
        ('S1TE', 'S1 Teknik Elektro'),
        ('S1TM', 'S1 Teknik Mesin'),
        ('S1TInd', 'S1 Teknik Industri'),
        ('S1TS', 'S1 Teknik Sipil'),
        ('S1Ars', 'S1 Arsitektur'),
        ('S1PWK', 'S1 Perencanaan Wilayah dan Kota'),
        ('S1TG', 'S1 Teknik Geologi'),
        ('S1TPM', 'S1 Teknik Perminyakan'),
        ('S1TPT', 'S1 Teknik Pertambangan'),
        ('S1DI', 'S1 Desain Interior'),
        ('S1DP', 'S1 Desain Produk'),
        ('S1DKV', 'S1 Desain Komunikasi Visual'),
        ('S1AL', 'S1 Arsitektur Lanskap'),
        ('S1TL', 'S1 Teknik Lingkungan'),
        ('S1Man', 'S1 Manajemen'),
        ('S1Ak', 'S1 Akuntansi'),
        ('S1EP', 'S1 Ekonomi Pembangunan'),
        ('S1Hukum', 'S1 Ilmu Hukum'),
        ('S1Kedokteran', 'S1 Kedokteran'),
        ('S1KedokteranGigi', 'S1 Kedokteran Gigi'),
        ('D3AkuntansiPerpajakan', 'D3 Akuntansi Perpajakan'),
    ]

    nama = models.CharField(max_length=100)
    nim = models.CharField(max_length=20, unique=True)
    tanggal_lahir = models.DateField()
    alamat = models.TextField()
    fakultas = models.CharField(max_length=10, choices=FAKULTAS_CHOICES)
    jurusan = models.CharField(max_length=20, choices=JURUSAN_CHOICES)
    program_studi = models.CharField(max_length=30, choices=PRODI_CHOICES)
    ipk = models.DecimalField(max_digits=3, decimal_places=2)
    prestasi = models.TextField(blank=True)
    keaktifan = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nama} ({self.nim})"

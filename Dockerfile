# Gunakan Python 3.12 image ringan
FROM python:3.12-slim

# Install dependensi sistem (termasuk distutils dan psycopg2 dependencies)
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-distutils \
    build-essential \
    libpq-dev \
    git \
    curl \
    libsdl2-dev \
    libfreetype6-dev \
    libjpeg-dev \
    libpng-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


# Atur direktori kerja di dalam container
WORKDIR /app

# Salin file requirements.txt terlebih dahulu untuk caching yang efisien
COPY requirements.txt .

# Install semua dependensi Python
RUN pip install --upgrade pip setuptools wheel && \
    pip install -r requirements.txt

# Salin semua file project ke dalam container
COPY . .

# Expose port yang digunakan oleh Django (default 8000)
EXPOSE 8000

# Jalankan perintah default (bisa diganti dengan gunicorn saat production)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

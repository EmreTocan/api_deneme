# Base image olarak Python 3.9 kullanıyoruz
FROM python:3.9-slim

# Çalışma dizini oluştur
WORKDIR /app

# Gereken dosyaları ekliyoruz
COPY requirements.txt .

# Gerekli bağımlılıkları kur
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama dosyalarını kopyala
COPY . .

# Port 8080'i aç
EXPOSE 8080

# Uygulamayı başlat
CMD ["python", "app.py"]

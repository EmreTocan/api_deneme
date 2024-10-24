# imaj olarak python arddınadan versiyonu ve gereksiz dosya ve kütüphanelerin olmadığı için daha az yer kaplayıp daha hızlı oolması için
FROM python:3.9-slim

# çalışma dizinidir çalışacağı dizini seçiyoruz
WORKDIR /app

# gereksinimleri imajın dizinine kopyalar 
COPY requirements.txt .

# gerekli python paketlerini kurması arından inen paketleri önbelleğe alınamsını engeller -r tüm paketleri tek komutla inmesini saplar dosyamızın içinde de ihtiyacımız olan paketler vardır 
RUN pip install --no-cache-dir -r requirements.txt

# bütün uygulama dosyalarını kopyalama 
COPY . .

# uygulama hani porttan dışa açılacağını ayarlıyoruz
EXPOSE 8080

# python ile hangi dosyamızı çalışacağını belirtiyoruz.
CMD ["python", "app.py"]

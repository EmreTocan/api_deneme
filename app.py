from flask import Flask, request

app = Flask(__name__)

# Toplama endpoint
@app.route('/toplama')
def toplama():
    try:
        # Query parametrelerini al ve virgül ile ayırarak liste yap
        parametreler = request.query_string.decode('utf-8').split(',')
        sayi1, sayi2 = map(int, parametreler)
        sonuc = sayi1 + sayi2
        return str(sonuc)
    except:
        return "Hata: Lütfen geçerli sayılar girin. Örnek: 2,2"

# Çıkarma endpoint
@app.route('/çıkarma')
def cikarma():
    try:
        parametreler = request.query_string.decode('utf-8').split(',')
        sayi1, sayi2 = map(int, parametreler)
        sonuc = sayi1 - sayi2
        return str(sonuc)
    except:
        return "Hata: Lütfen geçerli sayılar girin. Örnek: 2,2"

# Bölme endpoint
@app.route('/bölme')
def bolme():
    try:
        parametreler = request.query_string.decode('utf-8').split(',')
        sayi1, sayi2 = map(int, parametreler)
        if sayi2 == 0:
            return "Hata: 0'a bölme yapılamaz."
        sonuc = sayi1 / sayi2
        return str(sonuc)
    except:
        return "Hata: Lütfen geçerli sayılar girin. Örnek: 3,3"

# Çarpma endpoint
@app.route('/çarpma')
def carpma():
    try:
        parametreler = request.query_string.decode('utf-8').split(',')
        sayi1, sayi2 = map(int, parametreler)
        sonuc = sayi1 * sayi2
        return str(sonuc)
    except:
        return "Hata: Lütfen geçerli sayılar girin. Örnek: 2,3"

if __name__ == '__main__':
    app.run(debug=True, port=8080)

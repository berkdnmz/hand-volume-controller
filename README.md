
# El Hareketi ile Sistem Ses Kontrolü

Bu proje, el hareketlerini algılayarak bilgisayarın sistem sesini kontrol etmeyi sağlayan bir Python uygulamasıdır. Baş parmak ve işaret parmağı arasındaki mesafeye göre ses seviyesi artırılır veya azaltılır. Temassız ve arayüzsüz bir kontrol deneyimi sunar.

---

## İçindekiler

- [Genel Bakış](#genel-bakış)  
- [Özellikler](#özellikler)  
- [Kurulum](#kurulum)  
- [Kullanım](#kullanım)  
- [Dosya Yapısı](#dosya-yapısı)

---

## Genel Bakış

Uygulama, OpenCV ile kamera görüntüsünü işler, MediaPipe ile el parmaklarını algılar ve Pycaw aracılığıyla Windows sistem sesini kontrol eder. Baş parmak ile işaret parmağı ucu arasındaki mesafeye göre ses seviyesi dinamik olarak ayarlanır.

---

## Özellikler

- Gerçek zamanlı el takibi
- Baş parmak ve işaret parmağı arası mesafe ile ses kontrolü
- Kamera akışında canlı geri bildirim (çizgiler, daireler, yüzde gösterimi)
- %100 Python ile yazılmıştır
- Pycaw ile doğrudan sistem sesi kontrolü (Windows)

---

## Kurulum

1. Python 3.8 veya üzeri kurulu olmalı.
2. Gerekli paketleri yükleyin:

```bash
pip install opencv-python mediapipe numpy pycaw comtypes
```

> Not: `pycaw` sadece Windows sistemlerinde çalışır.

---

## Kullanım

Terminal veya komut satırında proje dizininde aşağıdaki komutu çalıştırın:

```bash
python main.py
```

Ardından:

- Kamera açılır ve elinizi algılar.
- Baş parmak ve işaret parmağını birbirinden uzaklaştırdıkça ses artar.
- Parmağı kapattıkça ses azalır.
- Sağ üstte ses yüzdesi gösterilir.
- `ESC` tuşuna basarak çıkabilirsiniz.

---

## Dosya Yapısı

```
.
├── main.py         # Ana Python dosyası
├── README.md       # Açıklama dosyası (bu dosya)
```

---

## Geliştirici

**Berk DÖNMEZ**

GitHub: [github.com/berkdnmz](https://github.com/berkdnmz)  
LinkedIn: [linkedin.com/in/berkdnmz](https://linkedin.com/in/berkdnmz)

---

**Temassız teknolojiyle etkileşimi artır!**

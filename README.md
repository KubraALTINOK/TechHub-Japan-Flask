# TechHub-Japan-Flask
Japonya'daki yazılım, yapay zeka ve Web 3.0 kariyer fırsatlarını tanıtan; Flask, Glassmorphism ve 3D Spline entegrasyonu ile geliştirilmiş fütüristik web uygulaması.

# 🎌 DevJapan Tech Hub: Fütüristik Kariyer Portalı

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![Spline 3D](https://img.shields.io/badge/Spline_3D-FF69B4?style=for-the-badge&logo=codeigniter&logoColor=white)

Geleneksel kültürün, fütüristik teknolojilerle buluştuğu noktayı keşfedin. **DevJapan Tech Hub**, Japonya'daki (özellikle Tokyo ve Osaka) yazılım ekosistemini, iş olanaklarını ve teknolojik AR-GE merkezlerini tanıtan çok sayfalı (Multi-Page) dinamik bir web uygulamasıdır.

## ✨ Öne Çıkan Özellikler

- **Dinamik Backend:** Proje iskeleti ve sayfa yönlendirmeleri **Python Flask** framework'ü ile oluşturulmuştur. Jinja2 şablon motoru kullanılarak veriler backend'den frontend'e dinamik olarak aktarılmıştır.
- **İnteraktif 3D Deneyimi:** Sayfa tasarımlarına entegre edilen **Spline 3D** motoru sayesinde, kullanıcı hareketlerine tepki veren fütüristik modeller eklenmiştir.
- **Modern UI/UX:** Arayüz tasarımında karanlık siberpunk teması ve şeffaf cam efekti (**Glassmorphism**) tercih edilerek kullanıcı odaklı, temiz ve dikkat çekici bir görünüm elde edilmiştir.
- **Modüler Şablon Mimarisi:** Her sayfa için kod tekrarı yapmak yerine, `base.html` üzerinden şablon kalıtımı (Template Inheritance) kullanılmıştır.

## 🚀 Kurulum ve Çalıştırma

Projeyi kendi bilgisayarınızda yerel bir sunucuda (localhost) çalıştırmak için aşağıdaki adımları izleyebilirsiniz.

**1. Projeyi klonlayın:**
```bash
git clone [https://github.com/KubraALTINOK/TechHub-Japan-Flask.git]
cd TechHub-Japan-Flask

2. Sanal ortam (Virtual Environment) oluşturun ve aktifleştirin:

Bash
# Windows için:
python -m venv .venv
.\.venv\Scripts\activate

# macOS / Linux için:
python3 -m venv .venv
source .venv/bin/activate

3. Gerekli kütüphaneleri yükleyin:

Bash
pip install flask

4. Flask sunucusunu başlatın:

Bash
python app.py

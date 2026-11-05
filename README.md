# 🎟️ Django Etkinlik Kayıt Sistemi

Kullanıcıların yaklaşan etkinlikleri inceleyebileceği, arama yapabileceği ve kontenjan dahilinde katılım kaydı oluşturup iptal edebileceği tam kapsamlı bir web uygulaması.

---

## 🚀 Özellikler

- **Kullanıcı Kimlik Doğrulama:** Kayıt olma (`Register`), güvenli oturum açma (`Login`) ve çıkış (`Logout`) mekanizması.
- **Etkinlik Vitrini:** Aktif etkinlikleri tarih sırasına göre listeleme.
- **Dinamik Arama:** Başlık ve konuma göre büyük/küçük harf duyarsız arama filtresi (`Q` nesneleri ile).
- **Kontenjan ve Doluluk Takibi:**
  - Kalan kontenjanı anlık hesaplama.
  - Doluluk oranına göre renk değiştiren dinamik Bootstrap doluluk çubuğu (`Progress Bar`).
- **Gelişmiş Doğrulama Kuralları:**
  - Tarihi geçmiş etkinlikleri otomatik algılama ve kayda kapatma.
  - Aynı kullanıcının aynı etkinliğe mükerrer kayıt yapmasını engelleme.
  - Kontenjan dolduğunda katılım butonunu pasife alma.
- **Profil ve Bilet Yönetimi (Etkinliklerim):** Katılınan etkinlikleri listeleme ve güvenli (IDOR korumalı) kayıt iptali.
- **Yönetim Paneli:** Django Admin ile etkinlik oluşturma, düzenleme ve katılımcı listesini görüntüleme.

---

## 🛠️ Kullanılan Teknolojiler

- **Backend:** Python 3.12, Django
- **Frontend:** HTML5, CSS3, Bootstrap 5
- **Veritabanı:** SQLite3
- **Versiyon Kontrol:** Git & GitHub

---

## 📦 Kurulum ve Çalıştırma

Projeyi yerel ortamınızda ayağa kaldırmak için aşağıdaki adımları izleyin:

### 1. Depoyu Klonlayın
```bash
git clone https://github.com/sevval-yvz/etkilik-kayit-sistemi.git
cd etkilik-kayit-sistemi
```

### 2. Sanal Ortamı Oluşturun ve Aktive Edin
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Gerekli Paketleri Yükleyin
```bash
pip install -r requirements.txt
```

### 4. Veritabanı Göçlerini Uygulayın
```bash
python manage.py migrate
```

### 5. Yönetici (Superuser) Hesabı Oluşturun (İsteğe bağlı)
```bash
python manage.py createsuperuser
```

### 6. Geliştirme Sunucusunu Başlatın
```bash
python manage.py runserver
```




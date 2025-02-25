# Pelacakan IP dengan Flask dan SQLite 
Proyek ini adalah aplikasi web sederhana untuk melacak lokasi berdasarkan **Alamat IP** menggunakan **ipinfo.io API**. Aplikasi ini dibangun dengan **Flask (Python)** dan menyimpan riwayat pencarian dalam **database SQLite**.  

---

## Fitur  
- Melacak lokasi berdasarkan **Alamat IP** yang diinputkan pengguna atau **IP otomatis** dari pengguna.  
- Menampilkan informasi geolokasi termasuk **kota, negara, ISP, koordinat**, dan **zona waktu**.  
- Menampilkan **abuse info** (jika tersedia dari API ipinfo.io).  
- Menyimpan **riwayat pencarian** dalam **SQLite**.  
- **Reset otomatis** pada database jika jumlah data mencapai **25 pencarian**.  
- Halaman **History** untuk melihat riwayat pencarian IP.  
- **Error page** jika data lokasi tidak ditemukan.  

---

## Teknologi yang Digunakan  
- **Flask**: Framework web untuk backend.  
- **SQLite**: Database lokal untuk menyimpan riwayat pencarian IP.  
- **SQLAlchemy ORM**: Untuk mempermudah manipulasi database.  
- **Jinja2 Template**: Untuk merender halaman HTML secara dinamis.  
- **ipinfo.io API**: Untuk mendapatkan data geolokasi berdasarkan IP.  

---

## Instalasi  
1. **Clone Repository**  
    ```bash
    git clone https://github.com/username/nama-repo.git
    cd nama-repo
    ```

2. **Buat Virtual Environment (Opsional tapi disarankan)**  
    ```bash
    python -m venv venv
    source venv/bin/activate   # Untuk MacOS/Linux
    .\venv\Scripts\activate   # Untuk Windows
    ```

3. **Instal Dependensi**  
    ```bash
    pip install Flask Flask-SQLAlchemy Flask-Migrate requests
    ```

4. **Atur API Key**  
    Daftar dan dapatkan **API Token** dari [ipinfo.io](https://ipinfo.io) lalu ganti di bagian berikut:  
    ```python
    ACCESS_TOKEN = 'ganti_dengan_token_anda'
    ```

5. **Migrasi Database**  
    ```bash
    flask db init
    flask db migrate -m "Inisialisasi database"
    flask db upgrade
    ```

6. **Jalankan Aplikasi**  
    ```bash
    flask run
    python app.py
    ```
    Aplikasi akan berjalan di **http://127.0.0.1:5000**.  

---

## Cara Menggunakan  
1. **Halaman Utama**  
   - Input **Alamat IP** yang ingin dilacak.  
   - Klik **"Lacak IP"** untuk melihat informasi lokasi.  
   - Jika tidak mengisi IP, aplikasi akan menggunakan **IP pengguna secara otomatis**.  

2. **Hasil Pelacakan**  
   - Menampilkan lokasi termasuk **kota, negara, ISP, koordinat**, dan **zona waktu**.  
   - Menampilkan **abuse info** jika tersedia.  

3. **Riwayat Pencarian**  
   - Klik **"History"** di navbar untuk melihat riwayat pencarian yang telah dilakukan.  
   - Database akan **di-reset otomatis** jika jumlah pencarian mencapai **25 data**.  

4. **Error Page**  
   - Jika **IP tidak ditemukan** atau **API tidak merespons**, halaman error akan ditampilkan.  

---
 
## **Struktur Direktori**  
```plaintext
Lacak-IP/
├── templates/
│   ├── index.html       # Halaman utama
│   └── history.html     # Halaman riwayat
├── static/              # File statis (CSS, JS, dll.)
├── app.py               # Main app Flask
├── models.py            # Model database
├── migrations/          # Folder migrasi database
├── venv/                # Virtual environment (tidak perlu di-push ke repo)
└── README.md            # Dokumentasi
```
---

## Contoh Hasil Pencarian  
IP Address: 8.8.8.8 Lokasi: Mountain View, California, US | Koordinat: 37.4056,-122.0775 | ISP: Google LLC | Zona Waktu: America/Los_Angeles Informasi Penyalahgunaan (Abuse): Nama: Google LLC | Alamat: Unknown | Negara: US | Email: abuse@google.com | Jaringan: 8.8.8.0/24 | Telepon: Unknown

---

## Catatan Penting  
- **API ipinfo.io** memiliki **rate limit** pada akun gratis. Jika mencapai batas, coba lagi setelah beberapa saat atau tingkatkan ke **akun berbayar**.  
- Data geolokasi **mungkin tidak akurat** tergantung pada penyedia layanan internet.  

---

## Lisensi  
Proyek ini dilisensikan di bawah **MIT License**. Silakan gunakan, modifikasi, dan distribusikan dengan bebas.  

---

## Kontribusi  
Kontribusi sangat diterima! Silakan:  
- **Fork** repository ini  
- Buat **branch** untuk fitur atau perbaikan baru (`git checkout -b fitur-baru`)  
- **Commit** perubahan (`git commit -m 'Tambah fitur baru'`)  
- **Push** ke branch (`git push origin fitur-baru`)  
- Buat **Pull Request**  

---

## Kontak  
Jika ada pertanyaan atau saran, silakan hubungi:  
- **Email 1**: [ritrama705@gmail.com](ritrama705@gmail.com)
- **Email 2**: [nabilmuhamad630@gmail.com](nabilmuhamad630@gmail.com) 
- **GitHub 1**: [IsFaktuear](https://github.com/IsFaktuear)
- **GitHub 2**: [Aaronabil](https://github.com/Aaronabil) 

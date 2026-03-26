# 🚀 Kayana Source Telegram Bot v1
**An Automation Tool by Azka Danish Kayana**

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Kayana Source v1** adalah bot Telegram berbasis Python yang memungkinkan kamu untuk mengontrol dan memonitor PC/Laptop secara remote. Cocok banget buat kamu yang mau akses file, buka aplikasi, atau sekadar intip layar PC pas lagi jauh dari meja.

---

## ✨ Fitur Utama (v1.0)

| Kategori | Perintah (Command) | Deskripsi |
| :--- | :--- | :--- |
| 🎬 **YouTube Explorer** | `yt [judul]` | Cari video, otomatis scroll, dan kirim screenshot ke Telegram. |
| 📱 **Messenger** | `telegram chat ke [nama] pesan [isi]` | Kirim pesan otomatis ke kontak di Telegram Desktop. |
| | `telegram buka chat [nama]` | Buka ruang chat spesifik (Standby mode). |
| 🌐 **Browser** | `buka chrome cari [query]` | Melakukan pencarian Google otomatis di Chrome. |
| | `tutup tab` | Menutup tab browser yang sedang aktif. |
| | `tutup chrome` | Menutup paksa seluruh aplikasi Google Chrome. |
| 🚀 **Apps & Files** | `buka app [nama]` | Menjalankan aplikasi (VS Code, Spotify, dll) via Windows Search. |
| | `tutup app [nama]` | Menutup aplikasi spesifik (Chrome, Spotify, Telegram, Discord). |
| | `buka [nama file]` | Mencari dan menjalankan file spesifik di dalam PC. |
| 📸 **Monitoring** | `screenshot` | Mengambil screenshot layar PC secara real-time. |
| ⚡ **Power** | `matikan laptop` | Melakukan Shutdown PC otomatis dengan delay 60 detik. |

---

## 🛠️ Persiapan Awal (Prerequisites)

Sebelum instalasi, pastikan kamu sudah menyiapkan:
1. **Python 3.10+** terinstall di PC.
2. **Telegram Desktop** dalam keadaan login (untuk fitur chat).
3. **API Token Bot** dari [@BotFather](https://t.me/BotFather).
4. **Chat ID** pribadi dari [@userinfobot](https://t.me/userinfobot) (agar orang lain tidak bisa bajak PC kamu).

---

## ⚙️ Instalasi & Setup

1. **Clone Repository**
   ```bash
   git clone [https://github.com/Azkadanishk/Kayana-Source-Telegram-Bot-v1.git](https://github.com/Azkadanishk/Kayana-Source-Telegram-Bot-v1.git)
   cd Kayana-Source-Telegram-Bot-v1
   
2. **Install Library yang Dibutuhkan**
   pip install python-telegram-bot pyautogui httpx

3. **Konfigurasi Script**
   Buka file main.py(nama file script kamu), cari bagian KONFIGURASI dan isi datanya:
   TELEGRAM_TOKEN = 'ISI_TOKEN_BOT_TELEGRAM'
   MY_CHAT_ID = 12345 #isi ID TELEGRAM DI @userinfobot

🚀 **Cara Menjalankan**

Cukup ketik perintah ini di terminal/CMD:
python main.py

Setelah bot aktif, buka Telegram kamu, cari bot yang kamu buat, lalu ketik /start untuk melihat menu panduan.

⚠️ **Disclaimer**
Project ini dibuat untuk tujuan pembelajaran dan produktivitas pribadi. Gunakan dengan bijak. Penulis tidak bertanggung jawab atas penyalahgunaan akses remote pada perangkat yang bukan milik pribadi.

🤝 **Kontribusi**
Punya ide fitur buat v2? Silakan buat Issue atau kirim Pull Request! Saya sangat terbuka buat kolaborasi.

**Made with ❤️ by Azka Danish Kayana**

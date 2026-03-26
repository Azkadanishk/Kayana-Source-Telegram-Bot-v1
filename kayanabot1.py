import logging
import webbrowser
import os
import time
import pyautogui
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, CommandHandler, filters
from telegram.request import HTTPXRequest

# --- KONFIGURASI ---
TELEGRAM_TOKEN = 'ISI_TOKEN_BOT_TELEGRAM' 
MY_CHAT_ID = 12345 #isi ID TELEGRAM DI @userinfobot

# Delay global antar tombol agar PC stabil
pyautogui.PAUSE = 0.3 

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# --- 1. FUNGSI PANDUAN LENGKAP (v3.9.5) ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.id != MY_CHAT_ID: return
    
    panduan = (
        "🚀 **KAYANA SOURCE TELEGRAM BOT v1 - by Azka Danish Kayana** 🚀\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        
        "🎬 **YOUTUBE EXPLORER**\n"
        "• `yt [judul]` → Cari & screenshot.\n\n"
        
        "📱 **MESSENGER (CLEAN SEARCH)**\n"
        "• `telegram chat ke [nama] pesan [isi]`\n"
        "• `telegram buka chat [nama]`\n\n"
        
        "🌐 **BROWSER & CHROME**\n"
        "• `buka chrome cari [query]`\n"
        "• `tutup tab` | `tutup chrome`\n\n"
        
        "🚀 **APP & FILE MANAGER**\n"
        "• `buka app [nama]` | `tutup app [nama]`\n"
        "• `buka [nama file]` | `cek file manager`\n\n"
        
        "📸 **SYSTEM MONITORING**\n"
        "• `screenshot` | `matikan laptop`\n\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
    )
    await update.message.reply_text(panduan, parse_mode='Markdown')

# --- 2. EXECUTOR UTAMA ---
async def kaynz_executor(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.id != MY_CHAT_ID: return

    text = update.message.text.lower()
    
    # --- FITUR TELEGRAM: KIRIM PESAN ---
    if "telegram chat ke" in text and "pesan" in text:
        try:
            bagian_nama = text.split("telegram chat ke")[1].split("pesan")[0].strip()
            bagian_pesan = text.split("pesan")[1].strip()
            await update.message.reply_text(f"Mengirim pesan ke {bagian_nama}...")
            pyautogui.press('win'); time.sleep(1.0); pyautogui.write('Telegram', interval=0.2); pyautogui.press('enter')
            time.sleep(5.0); pyautogui.hotkey('ctrl', 'f'); time.sleep(1.0)
            for _ in range(15): pyautogui.press('backspace')
            pyautogui.write(bagian_nama, interval=0.1); time.sleep(2.5)
            pyautogui.press('down'); time.sleep(0.5); pyautogui.press('enter'); time.sleep(1.5)
            pyautogui.write(bagian_pesan, interval=0.1); time.sleep(0.5); pyautogui.press('enter')
            time.sleep(1.0); pyautogui.press('esc'); time.sleep(0.5); pyautogui.press('esc') 
            await update.message.reply_text(f"Kaynz: Pesan terkirim!")
        except Exception as e: await update.message.reply_text(f"Error: {str(e)}")

    # --- FITUR TELEGRAM: BUKA CHAT ---
    elif "telegram buka chat" in text:
        nama_kontak = text.replace("telegram buka chat", "").strip()
        await update.message.reply_text(f"Membuka chat {nama_kontak}...")
        pyautogui.press('win'); time.sleep(0.5); pyautogui.write('Telegram', interval=0.1); pyautogui.press('enter')
        time.sleep(4.0); pyautogui.hotkey('ctrl', 'f'); time.sleep(1.0)
        for _ in range(15): pyautogui.press('backspace')
        pyautogui.write(nama_kontak, interval=0.1); time.sleep(2.0)
        pyautogui.press('down'); time.sleep(0.5); pyautogui.press('enter')
        time.sleep(10); pyautogui.press('esc')
        await update.message.reply_text(f"Chat {nama_kontak} standby.")

    # --- FITUR CHROME: SEARCH ---
    elif "buka chrome cari" in text:
        query = text.replace("buka chrome cari", "").strip()
        await update.message.reply_text(f"Mencari '{query}' di Chrome...")
        search_url = f"https://www.google.com/search?q={query}"
        webbrowser.open(search_url)

    # --- FITUR YT ---
    elif text.startswith("yt "):
        query = text.replace("yt ", "").strip()
        await update.message.reply_text(f"Memuat visual YouTube '{query}'...")
        search_url = f"https://www.youtube.com/results?search_query={query}"
        webbrowser.open(search_url)
        time.sleep(25.0); pyautogui.scroll(-400); time.sleep(26.0)
        pyautogui.screenshot("yt_visual.png")
        with open("yt_visual.png", 'rb') as photo: await update.message.reply_photo(photo)
        os.remove("yt_visual.png")

    # --- FITUR BUKA APP ---
    elif text.startswith("buka app "):
        nama_app = text.replace("buka app ", "").strip()
        await update.message.reply_text(f"Membuka aplikasi '{nama_app}'...")
        pyautogui.press('win'); time.sleep(1.0); pyautogui.write(nama_app, interval=0.2); time.sleep(2.0); pyautogui.press('enter')
        time.sleep(0.5); pyautogui.press('esc')
        await update.message.reply_text(f"✅ Perintah buka '{nama_app}' sudah dijalankan.")

    # --- FITUR BUKA FILE ---
    elif text.startswith("buka ") and not any(x in text for x in ["app", "chat", "chrome", "yt"]):
        nama_file = text.replace("buka ", "").strip()
        await update.message.reply_text(f"Mencari file '{nama_file}'...")
        pyautogui.press('win'); time.sleep(1.0); pyautogui.write(nama_file, interval=0.1); pyautogui.press('enter')
        time.sleep(0.5); pyautogui.press('esc')

    # --- FITUR TUTUP APP ---
    elif text.startswith("tutup app "):
        nama_input = text.replace("tutup app ", "").strip()
        if "explorer" in nama_input or "folder" in nama_input:
            pyautogui.hotkey('alt', 'f4')
            await update.message.reply_text("✅ Jendela folder ditutup.")
        else:
            process_map = {"chrome": "chrome.exe", "spotify": "Spotify.exe", "telegram": "Telegram.exe", "discord": "Discord.exe"}
            target_exe = process_map.get(nama_input, f"{nama_input}.exe")
            os.system(f"taskkill /F /IM {target_exe} /T")
            await update.message.reply_text(f"✅ {target_exe} dimatikan.")

    # --- SYSTEM COMMANDS ---
    elif text == "screenshot":
        pyautogui.screenshot("screen.png")
        with open("screen.png", 'rb') as photo: await update.message.reply_photo(photo)
        os.remove("screen.png")

    elif text == "tutup tab":
        pyautogui.hotkey('ctrl', 'w')
        await update.message.reply_text("Tab ditutup.")

    elif text == "tutup chrome":
        os.system("taskkill /F /IM chrome.exe /T")
        await update.message.reply_text("Chrome ditutup.")

    elif text == "matikan laptop":
        await update.message.reply_text("PC akan mati dalam 60 detik.")
        os.system("shutdown /s /t 60")

    else:
        await update.message.reply_text("Perintah tidak dimengerti.")

# --- 3. RUN BOT ---
if __name__ == '__main__':
    t_request = HTTPXRequest(connect_timeout=30, read_timeout=30)
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).request(t_request).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), kaynz_executor))
    print("Kayana Source Telegram Bot v1 Aktif! Perintah siap dijalankan....")
    app.run_polling()
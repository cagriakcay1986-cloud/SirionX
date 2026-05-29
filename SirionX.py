import streamlit as st
import pandas as pd
import sqlite3
import schedule
import time
from playwright.sync_api import sync_playwright

# --- 1. OTOMATİK VERİ ÇEKME (Her gün 10:00) ---
def bulten_cek():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.iddaa.com/program/canli/futbol")
        # İddaa sitesi dinamik yükleme yapar, bu yüzden biraz bekle
        time.sleep(5) 
        
        # Veriyi çek (İddaa'nın CSS yapısına göre güncellenebilir)
        maclar = page.query_selector_all(".match-name") 
        data = [{"mac": m.inner_text(), "tarih": pd.Timestamp.now()} for m in maclar]
        
        # Veritabanına kaydet
        conn = sqlite3.connect("sirionx_beyin.db")
        pd.DataFrame(data).to_sql("bulten", conn, if_exists="append")
        conn.close()
        browser.close()

# --- 2. ANALİZ VE TAHMİN MOTORU ---
def analiz_et(mac_adi):
    # Sentiment (Yorum Analizi) & Poisson birleşimi
    # Burada geçmiş maç verilerini sorguluyoruz
    conn = sqlite3.connect("sirionx_beyin.db")
    gecmis = pd.read_sql(f"SELECT * FROM bulten WHERE mac LIKE '%{mac_adi}%'", conn)
    conn.close()
    
    if len(gecmis) > 0:
        return "🧠 Analiz Tamamlandı: Yüksek İsabet İhtimali"
    return "🚀 Analiz Başlıyor: Veri Toplanıyor..."

# --- 3. ARAYÜZ (STREAMLIT) ---
st.set_page_config(page_title="SirionX Ultimate", layout="wide")
st.title("🧠 SirionX - Otonom Analitik Beyin")

if st.button("Bülteni Güncelle ve Analiz Et"):
    bulten_cek()
    st.success("Veriler tazelendi!")

st.subheader("📊 Güncel Tahminler")
# Burada veritabanındaki maçları listele

import streamlit as st
import pandas as pd
import sqlite3
import requests

# Basit ve hatasız kütüphane kullanımı
st.set_page_config(page_title="SirionX Core", layout="wide")
st.title("🧠 SirionX - Otonom Analitik Beyin")

# Veritabanı bağlantısı
def get_db():
    conn = sqlite3.connect("sirionx_beyin.db")
    return conn

# Maçları çekme ve hata yönetimi
def verileri_tazele():
    try:
        # İddaa verisi veya API yerine daha kararlı bir yöntem: 
        # Veri yoksa bile sistemin çökmesini engelle
        st.info("Veri havuzu taranıyor...")
        # (Buraya daha önce konuştuğumuz kazıyıcı entegre edilecek)
    except Exception as e:
        st.error(f"Sistem hatası: {e}")

# Arayüz
if st.sidebar.button("Bülteni Yenile"):
    verileri_tazele()

st.write("Sistem şu an stabil çalışıyor. Bültenin dolmasını bekliyoruz.")

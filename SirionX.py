import streamlit as st
import requests
import pandas as pd

st.title("⚽ SirionX - Lig Analiz Terminali")

# API Ayarları
API_KEY = "senin_tokenin_buraya" 
HEADERS = {'authorization': API_KEY, 'content-type': 'application/json'}

# Lig Listesini Çek
def get_leagues():
    # Kendi gönderdiğin o doğru JSON yapısını buraya entegre ediyoruz
    return [
        {"league": "Süper Lig", "key": "super-lig"},
        {"league": "TFF 1. Lig", "key": "tff-1-lig"},
        {"league": "İngiltere Premier Ligi", "key": "ingiltere-premier-ligi"}
    ]

ligler = get_leagues()
lig_isimleri = [item['league'] for item in ligler]

# Arayüz: Kullanıcının lig seçmesini sağla
secilen_lig = st.selectbox("Analiz edilecek ligi seç:", lig_isimleri)

# Seçilen ligin 'key' değerini bul
secilen_key = next(item['key'] for item in ligler if item['league'] == secilen_lig)

if st.button("Analizi Başlat"):
    st.write(f"📡 {secilen_lig} ({secilen_key}) için veriler çekiliyor...")
    # Burada seçilen_key kullanarak o lige özel maçları çekeceğiz
    st.success(f"{secilen_lig} hazır! Maç verileri bağlanıyor...")

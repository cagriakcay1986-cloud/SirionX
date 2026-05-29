import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="SirionX Ultimate", layout="wide")
st.title("🧠 SirionX - Analitik Terminal (Final)")

# Hata yutucu veri çekme fonksiyonu
def veri_cek():
    try:
        # Doğrudan engelsiz veri kaynağı
        url = "https://www.scorebat.com/video-api/v3/"
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.json().get('response', [])
        return None
    except:
        return None

if st.button("Sistemi Başlat"):
    with st.spinner("Veri hattı kuruluyor..."):
        data = veri_cek()
        if data:
            st.success("✅ Veri Akışı Başarılı!")
            df = pd.DataFrame(data)
            # İsteğe göre tahmin motorunu buraya bağlayacağız
            st.table(df[['title', 'competition', 'date']])
        else:
            st.error("❌ Veri hattına ulaşılamadı. Lütfen sunucu durumunu kontrol et.")

import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup

st.title("🧠 SirionX - Veri Hattı Dedektörü")

def verileri_tazele():
    try:
        # İddaa bültenini doğrudan çekmek yerine daha genel bir spor kaynağı kullanalım
        url = "https://www.mackolik.com/canli-sonuclar" # Alternatif en güvenilir kaynak
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # Maç isimlerini çeken genel bir seçici
            maclar = soup.find_all(class_='match-name') 
            if maclar:
                for m in maclar[:5]: # İlk 5 maçı göster
                    st.write(f"✅ Bulunan Maç: {m.text.strip()}")
            else:
                st.warning("Sayfa yüklendi ama maç listesine ulaşılamadı. HTML yapısı değişmiş olabilir.")
        else:
            st.error(f"Bağlantı hatası: {response.status_code}")
    except Exception as e:
        st.error(f"Kritik Hata: {e}")

if st.button("Veri Hattını Zorla"):
    verileri_tazele()

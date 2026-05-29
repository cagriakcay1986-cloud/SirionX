import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup

st.title("⚽ SirionX - Otonom İddaa Bülteni")

def veriyi_cek():
    url = "https://www.iddaa.com/program/canli/futbol"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # İddaa'nın maç isimlerini tutan class yapısı
        maclar = soup.select(".match-name") 
        data = [{"Maç": m.text.strip()} for m in maclar]
        
        return pd.DataFrame(data)
    except Exception as e:
        return None

if st.button("Bülteni Çek"):
    df = veriyi_cek()
    if df is not None and not df.empty:
        st.table(df)
    else:
        st.error("Veri çekilemedi. İddaa sitesi bot koruması uyguluyor olabilir.")

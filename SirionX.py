import streamlit as st
import requests
import pandas as pd
from bs4 import BeautifulSoup

st.title("🧠 SirionX - Otonom Analitik")

def bulten_cek():
    try:
        url = "https://www.iddaa.com/program/canli/futbol"
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Veri çekme mantığın buraya gelecek
        st.write("Veri hattı aktif.")
    except Exception as e:
        st.error(f"Hata: {e}")

if st.button("Sistemi Senkronize Et"):
    bulten_cek()

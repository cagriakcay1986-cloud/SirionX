import streamlit as st
import requests
import pandas as pd

st.title("⚽ SirionX - Veri Dedektörü")

# API Anahtarlarını buraya gir
API_KEY = "buraya_kendi_anahtarini_yapistir"
HEADERS = {
    "x-rapidapi-key": API_KEY,
    "x-rapidapi-host": "api-football-v1.p.rapidapi.com"
}

def veri_test_et():
    url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"
    querystring = {"live": "all"}
    try:
        response = requests.get(url, headers=HEADERS, params=querystring)
        return response.json()
    except Exception as e:
        return f"Hata: {e}"

if st.button("Veriyi Analiz Et"):
    data = veri_test_et()
    # Gelen ham veriyi ekranda görerek yapıyı teşhis edelim
    st.json(data)

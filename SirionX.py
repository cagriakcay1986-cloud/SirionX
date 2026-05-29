import streamlit as st
import requests
import pandas as pd

st.title("⚽ SirionX - Profesyonel Lig Listesi")

# Buraya kendi token'ını yapıştır
API_KEY = "apikey senin_tokenin_buraya" 
URL = "https://api.collectapi.com/sport/leaguesList"

def get_leagues():
    headers = {
        'authorization': API_KEY,
        'content-type': 'application/json'
    }
    try:
        response = requests.get(URL, headers=headers, timeout=10)
        if response.status_code == 200:
            return response.json().get('result', [])
        else:
            return f"Hata: {response.status_code}"
    except Exception as e:
        return str(e)

if st.button("Ligleri Listele"):
    data = get_leagues()
    if isinstance(data, list):
        st.success("Ligler başarıyla çekildi!")
        st.table(pd.DataFrame(data))
    else:
        st.error(data)

import streamlit as st
import pandas as pd

st.title("⚽ SirionX - Otonom İddaa Analiz")

try:
    df = pd.read_csv("tahminler.csv")
    st.table(df)
except:
    st.info("Analiz sonuçları bekleniyor... GitHub Actions'ı çalıştır.")

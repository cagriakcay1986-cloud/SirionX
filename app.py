import streamlit as st
import pandas as pd

st.title("⚽ SirionX - Analitik Terminal")

try:
    df = pd.read_csv("maclar.csv")
    st.table(df)
except:
    st.warning("Henüz bülten çekilmedi. GitHub Actions'ı çalıştır.")

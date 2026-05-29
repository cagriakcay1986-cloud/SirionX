import streamlit as st
import pandas as pd
import os

st.title("⚽ SirionX - Analiz Terminali")

# Dosyanın olduğu klasörü belirt
file_path = os.path.join(os.getcwd(), "maclar.csv")

if os.path.exists(file_path):
    df = pd.read_csv(file_path)
    if not df.empty:
        st.success("Veri başarıyla yüklendi!")
        st.dataframe(df)
    else:
        st.warning("CSV dosyası boş görünüyor.")
else:
    st.error(f"Hata: Dosya bulunamadı! Aranan yol: {file_path}")
    st.write("Mevcut dosyalar:", os.listdir('.'))

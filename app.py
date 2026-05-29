import streamlit as st
import pandas as pd
import os

st.title("⚽ SirionX - Analiz Terminali")

# Dosya yolunu kesinleştir
csv_yolu = "maclar.csv"

if os.path.exists(csv_yolu):
    try:
        df = pd.read_csv(csv_yolu)
        if not df.empty:
            st.write("Veri Başarıyla Yüklendi:")
            st.table(df)
        else:
            st.warning("CSV dosyası mevcut ama içinde veri yok!")
    except Exception as e:
        st.error(f"Dosya okuma hatası: {e}")
else:
    st.error(f"Dosya bulunamadı: {os.path.abspath(csv_yolu)}")
    st.write("Depodaki dosyalar:", os.listdir('.'))

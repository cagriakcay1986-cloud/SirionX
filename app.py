import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="SirionX Maç Bülteni", layout="wide")

st.title("⚽ SirionX - Güncel Maç Bülteni")

# CSV dosyasının varlığını kontrol et
if os.path.exists("maclar.csv"):
    df = pd.read_csv("maclar.csv")
    
    # Tabloyu şık bir şekilde göster
    st.dataframe(df, use_container_width=True)
    
    # İstersen veriyi indirme butonu ekle
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("CSV Olarak İndir", csv, "maclar.csv", "text/csv")
else:
    st.warning("Veri henüz çekilmedi. Lütfen GitHub Actions'ı çalıştır.")

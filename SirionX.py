import streamlit as st
import pandas as pd
from playwright.sync_api import sync_playwright

st.set_page_config(page_title="SirionX - Otonom Bülten", layout="wide")
st.title("⚽ SirionX - Kendi Bültenini Oluştur")

def bulten_kaziyici():
    with st.spinner("Bülten taranıyor..."):
        try:
            with sync_playwright() as p:
                browser = p.chromium.launch(headless=True)
                page = browser.new_page()
                # İddaa canlı futbol sayfasına git
                page.goto("https://www.iddaa.com/program/canli/futbol", timeout=60000)
                
                # Sayfanın yüklenmesini bekle
                page.wait_for_timeout(5000)
                
                # Verileri yakala (İddaa'nın CSS class isimlerine göre)
                # Not: Bu class isimleri zamanla değişirse sayfayı inceleyip güncelleyeceğiz
                maclar = page.query_selector_all(".match-name") 
                data = [{"Maç": m.inner_text()} for m in maclar]
                
                browser.close()
                return pd.DataFrame(data)
        except Exception as e:
            return f"Hata: {e}"

if st.button("Her Sabah 10:00 Bültenini Çek"):
    df = bulten_kaziyici()
    if isinstance(df, pd.DataFrame) and not df.empty:
        st.success("Bülten Başarıyla Çekildi!")
        st.table(df)
    else:
        st.error("Veri alınamadı. İddaa sitesi bot korumasını sıkılaştırmış olabilir.")

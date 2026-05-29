import streamlit as st
import pandas as pd
import sqlite3

st.title("🧠 SirionX - Canlı Analitik Terminal")

# 1. Kendi Veritabanını Oluştur
def veritabanini_kur():
    conn = sqlite3.connect("sirionx_data.db")
    # Eğer tablon yoksa oluştur
    conn.execute("CREATE TABLE IF NOT EXISTS maclar (tarih TEXT, ev_sahibi TEXT, deplasman TEXT, tahmin TEXT)")
    conn.commit()
    conn.close()

# 2. Veri Ekleme Paneli (Artık veriyi sen elle veya bir txt dosyasıyla sisteme "enjekte" edeceksin)
with st.expander("📊 Yeni Maç Verisi Ekle"):
    ev = st.text_input("Ev Sahibi")
    dep = st.text_input("Deplasman")
    if st.button("Veritabanına Kaydet"):
        conn = sqlite3.connect("sirionx_data.db")
        conn.execute("INSERT INTO maclar (ev_sahibi, deplasman) VALUES (?, ?)", (ev, dep))
        conn.commit()
        conn.close()
        st.success("Veri sisteme enjekte edildi!")

# 3. Poisson Analiz Motorunu Çalıştır
if st.button("Sistemi Başlat (Tahminleri Gör)"):
    conn = sqlite3.connect("sirionx_data.db")
    df = pd.read_sql("SELECT * FROM maclar", conn)
    conn.close()
    
    if not df.empty:
        st.write("Analiz ediliyor...")
        # Burada Poisson formülünü df üzerindeki ev/dep takımlarına uygularız
        st.table(df)
    else:
        st.info("Veritabanı boş, lütfen maç verisi ekle.")

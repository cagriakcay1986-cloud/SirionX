import streamlit as st
import pandas as pd
import os
import time

st.set_page_config(page_title="SirionX Terminali", layout="wide")

st.title("⚽ SirionX - Otonom Analiz")

# 1. Aşama: Dosyanın nerede olduğunu kesinleştir
st.subheader("Veri Durumu")
csv_yolu = "maclar.csv"
absolut_yol = os.path.abspath(csv_yolu)

st.write(f"Aranan dosya yolu: `{absolut_yol}`")

# 2. Aşama: Dosya var mı?
if os.path.exists(csv_yolu):
    st.success(f"Buldum! {csv_yolu} dosyası mevcut.")
    
    # 3. Aşama: Okumayı dene
    try:
        df = pd.read_csv(csv_yolu)
        
        # Dosya boş mu?
        if not df.empty:
            st.subheader(f"Güncel Bülten ({len(df)} Maç)")
            st.dataframe(df, use_container_width=True)
            st.info(f"Son güncelleme saati (Terminal saati): {time.ctime(os.path.getmtime(csv_yolu))}")
        else:
            st.warning("⚠️ Dosya mevcut ama içi boş!")
    
    except Exception as e:
        st.error(f"❌ Dosya okuma hatası: {e}")
        st.write("Bu hata, dosyanın formatının bozuk olduğunu veya kilitli olduğunu gösterir.")

else:
    st.error(f"❌ Dosya bulunamadı: {csv_yolu}")
    st.write("GitHub Actions yeşil tik vermiş olabilir ama bu uygulama sunucusunda dosya mevcut değil.")
    
    # Kök dizindeki dosyaları listele (Hata tespiti için)
    st.write("Mevcut dizindeki dosyalar:", os.listdir('.'))
    
    st.info("Lütfen Streamlit Cloud panelinden 'Manage app' -> 'Re-deploy' yapmayı dene.")

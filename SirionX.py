import streamlit as st
import pandas as pd
import random

# SirionX Başlık ve Tema Ayarları
st.set_page_config(page_title="SirionX Multi-Analyst", layout="wide")
st.title("🤖 SirionX v1.4 - Çoklu Varlık ve Yatırım Organizması")
st.markdown("---")

# 1. SIDEBAR - BAĞIMSIZ PARAMETRELER
st.sidebar.header("⚙️ SirionX Kontrol Merkezi")

# İddaa Parametreleri (Dokunulmadı, Aynen Korunuyor)
st.sidebar.subheader("⚽ İddaa Beyin Ayarları")
ofans_kat = st.sidebar.slider("Ofansif Güç Katsayısı", 0.5, 2.0, 1.15)
defans_kat = st.sidebar.slider("Defansif Zaafiyet Katsayısı", 0.5, 2.0, 0.95)

# Borsa ve Kripto Parametreleri (Yeni Odalar)
st.sidebar.subheader("📈 Finansal Risk Ayarları")
korku_esigi = st.sidebar.slider("Yapay Zekâ Korku Hassasiyeti", 10, 90, 25)

# 2. SABİT VERİ SETLERİ (İddaa Maçlarınız Aynen Korunuyor)
gercek_bulten = [
    {"Maç Kodu": "40101", "Lig": "Kolombiya Premier", "Ev Sahibi": "Real Soacha", "Deplasman": "R Aguilas", "MS1": 2.40, "MSX": 2.95, "MS2": 2.45},
    {"Maç Kodu": "40102", "Lig": "Copa Libertadores", "Ev Sahibi": "Millonarios", "Deplasman": "O'Higgins", "MS1": 1.65, "MSX": 3.40, "MS2": 3.80},
    {"Maç Kodu": "40103", "Lig": "Copa Sudamericana", "Ev Sahibi": "LDU Quito", "Deplasman": "Always Ready", "MS1": 1.35, "MSX": 4.10, "MS2": 5.50},
    {"Maç Kodu": "40104", "Lig": "Uluslararası Hazırlık", "Ev Sahibi": "Crystal Palace", "Deplasman": "Rayo Vallecano", "MS1": 1.85, "MSX": 3.25, "MS2": 3.20}
]

# 3. YENİ MAKRO FİNANSAL VERİLER (Simüle Makro Endeksler)
makro_endeksler = [
    {"Endeks": "BIST 100 (Borsa İstanbul)", "Mevcut Değer": "10,250", "Günlük Değişim": "+%1.20", "Piyasa Durumu": "Dengeli Alıcılı", "SirionX Stratejisi": "Kademeli Hisse Alımı Uygun"},
    {"Endeks": "S&P 500 (ABD Borsası)", "Mevcut Değer": "5,120", "Günlük Değişim": "-%0.45", "Piyasa Durumu": "Düzeltme Eğilimi", "SirionX Stratejisi": "Nakit Korunmalı, İzle"},
    {"Endeks": "Bitcoin Dominansı (BTC.D)", "Mevcut Değer": "%54.20", "Günlük Değişim": "+%0.80", "Piyasa Durumu": "Para BTC'ye Akıyor", "SirionX Stratejisi": "Altcoinlerden Uzak Dur, BTC Tut"}
]

# 4. YARDIMCI FONKSİYONLAR (Hata düzeltmeli fonksiyonlar aynen korundu)
def yorum_analizi_yap(mac_kodu):
    internet_yorumlari = {
        "40101": ["Real Soacha evinde kapanarak oynuyor.", "R Aguilas deplasmanda risk almaz."],
        "40102": ["Millonarios evinde Bogota rakım avantajına sahip.", "O'Higgins savunmasında iki as oyuncu cezalı."],
        "40103": ["LDU Quito evinde boğuyor.", "Always Ready deplasmanda kırılgan, gol şov olur."],
        "40104": ["Crystal Palace hazırlık maçında ofansif.", "Vallecano kontra kovalar."]
    }
    yorumlar = internet_yorumlari.get(mac_kodu, [])
    if not yorumlar: return 0.0
    pozitif, negatif = ["baskılı", "gol şov", "üst", "bol gol", "ofansif"], ["kapanarak", "az gol", "cezalı", "kırılgan"]
    skor = 0
    for y in yorumlar:
        yk = y.lower()
        for p in pozitif:
            if p in yk: skor += 0.25
        for n in negatif:
            if n in yk: skor -= 0.25
    return round(skor, 2)

def takim_istatistik_hesapla(takim_adi):
    random.seed(sum(ord(c) for c in takim_adi))
    if takim_adi in ["LDU Quito", "Millonarios"]: return 2.2 * ofans_kat, 0.8 * defans_kat
    elif takim_adi in ["Real Soacha", "O'Higgins"]: return 1.0 * ofans_kat, 1.5 * defans_kat
    return 1.5 * ofans_kat, 1.2 * defans_kat

# 5. YENİLENEN ÇOKLU MENÜ YAPISI (ANA EKRAN)
ana_sekme1, ana_sekme2, ana_sekme3 = st.tabs(["⚽ İDDİA MODÜLÜ", "📈 BORSA MAKRO MOTORU", "🪙 KRİPTO DÖNGÜ DEDEKTÖRÜ"])

# --- SEKME 1: İDDİA (Eksiksiz Sürümünüz Korundu) ---
with ana_sekme1:
    st.subheader("SirionX Canlı İddaa Tahminleri ve Analizleri")
    tahmin_havuzu = []
    for mac in gercek_bulten:
        ev, dep, kod = mac["Ev Sahibi"], mac["Deplasman"], mac["Maç Kodu"]
        ev_of, ev_def = takim_istatistik_hesapla(ev)
        dep_of, dep_def = takim_istatistik_hesapla(dep)
        gol_beklentisi = ((ev_of + dep_def + dep_of + ev_def) / 2) + (yorum_analizi_yap(kod) * 0.6)
        tahmin = "2.5 ÜST" if gol_beklentisi >= 2.45 else ("2.5 ALT" if gol_beklentisi <= 1.85 else "KG VAR")
        tahmin_havuzu.append({
            "Kod": kod, "Lig": mac["Lig"], "Maç": f"{ev} - {dep}",
            "SirionX Gol Beklentisi": round(max(0, gol_beklentisi), 2), "SirionX Önerisi": tahmin
        })
    st.dataframe(pd.DataFrame(tahmin_havuzu), use_container_width=True)
    st.info("⏱️ Maçlar bittiğinde skorları buraya işleyip evrim döngüsünü tetikleyeceğiz.")

# --- SEKME 2: BORSA (Yeni Oda) ---
with ana_sekme2:
    st.subheader("📊 Küresel ve Yerel Borsa Endeks Analizi")
    st.markdown("SirionX makro borsa motoru, endekslerin tepe ve dip döngülerini tarar.")
    st.table(pd.DataFrame(makro_endeksler))
    
    # Basit bir indikatör simülasyonu
    st.markdown("### 🚨 SirionX Borsa Erken Uyarı Sistemi")
    st.warning("BIST 100 endeksinde hacimli yükseliş devam ediyor ancak S&P 500 düzeltme sinyali veriyor. Yeni pozisyon açarken temkinli olunmalıdır.")

# --- SEKME 3: KRİPTO (Yeni Oda) ---
with ana_sekme3:
    st.subheader("🪙 Kripto Para Döngü Kontrol Paneli")
    
    # Kripto Korku ve Açgözlülük Metriği
    korku_skoru = 74 # Şimdilik sabit simüle değer
    st.metric("Piyasa Korku ve Açgözlülük Endeksi (Fear & Greed)", f"{korku_skoru} / 100", "AŞIRI AÇGÖZLÜLÜK DÖNEMİ")
    
    if korku_skoru > 70:
        st.error("⚠️ SIRIONX KRİPTO UYARISI: Piyasa aşırı coşkulu (FOMO) döneminde. Balinaların kar satışı yapma ihtimali yüksek. Dipten mal toplama evresine geçene kadar nakit oranını artırın.")
    else:
        st.success("✅ SIRIONX KRİPTO UYARISI: Piyasa korku ikliminde, dipten toplama için ideal koridor.")

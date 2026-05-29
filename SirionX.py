import pandas as pd
import random

def analiz_motoru(mac_adi):
    # BURASI GELİŞTİRİLECEK: 
    # Buraya geçmiş maç sonuçlarını (CSV/Excel) okuyup 
    # Poisson dağılımı uygulayan kodunu ekleyeceğiz.
    # Şimdilik prototip olarak:
    olasilik = random.uniform(60, 95) 
    return round(olasilik, 2)

def main():
    try:
        # 1. Adım: Veriyi oku
        df = pd.read_csv("maclar.csv")
        
        # 2. Adım: Analiz et
        df['Tahmin_Olasilik'] = df['mac'].apply(analiz_motoru)
        
        # 3. Adım: Sonucu kaydet
        df.to_csv("tahminler.csv", index=False)
        print("Analiz motoru başarıyla çalıştı.")
    except Exception as e:
        print(f"Analiz hatası: {e}")

if __name__ == "__main__":
    main()

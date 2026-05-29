import pandas as pd
import requests
from bs4 import BeautifulSoup
import os

def bulten_cek():
    # İddaa verisini çekmek için yapılandırılmış başlıklar
    url = "https://www.iddaa.com/program/canli/futbol"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status() # Hata oluşursa yakala
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Maç isimlerini çeken seçici (Bu seçici İddaa'nın yapısına göre güncel tutulmalı)
        maclar_raw = soup.select(".match-name")
        maclar = [{"mac": m.text.strip()} for m in maclar_raw]
        
        # Eğer maç bulunamazsa CSV'yi boş oluşturma
        if maclar:
            df = pd.DataFrame(maclar)
            df.to_csv("maclar.csv", index=False)
            print(f"Başarılı! {len(maclar)} maç kaydedildi.")
        else:
            print("Uyarı: Maç verisi bulunamadı, HTML yapısı değişmiş olabilir.")
            
    except Exception as e:
        print(f"Hata oluştu: {e}")

if __name__ == "__main__":
    bulten_cek()

import pandas as pd
import requests
from bs4 import BeautifulSoup
import os

def bulten_cek():
    url = "https://www.iddaa.com/program/canli/futbol"
    # Tarayıcı taklidi yapmak için daha gelişmiş başlıklar
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Seçicimizi daha genel tutalım
        maclar = [m.text.strip() for m in soup.select(".match-name")]
        
        if not maclar:
            # HATA DURUMU: Maç çekilemediyse içine ipucu yazalım
            df = pd.DataFrame(["HATA: Veri cekilemedi, secici degismis olabilir"], columns=["mac"])
            df.to_csv("maclar.csv", index=False)
        else:
            df = pd.DataFrame(maclar, columns=["mac"])
            df.to_csv("maclar.csv", index=False)
            print(f"Başarılı: {len(maclar)} maç çekildi.")
            
    except Exception as e:
        # HATA DURUMU: Siteye erişim hatası
        df = pd.DataFrame([f"HATA: {str(e)}"], columns=["mac"])
        df.to_csv("maclar.csv", index=False)

if __name__ == "__main__":
    bulten_cek()

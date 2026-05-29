import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

# 1. VERİ ÇEKME (Scraping)
def bulten_cek():
    url = "https://www.iddaa.com/program/canli/futbol"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Maç isimlerini al
    maclar = [{"mac": m.text.strip()} for m in soup.select(".match-name")]
    
    df = pd.DataFrame(maclar)
    df.to_csv("maclar.csv", index=False)
    return df

# 2. ANALİZ MOTORU
def analiz_et(df):
    # Burada "Gerçek Veri" ile Poisson veya istatistiksel ağırlıklandırma yapacağız
    # Şimdilik prototip olarak rastgele bir olasılık atıyoruz
    df['Tahmin_Olasilik'] = np.random.uniform(60, 95, size=len(df)).round(2)
    df.to_csv("tahminler.csv", index=False)
    print("Analiz tamamlandı!")

if __name__ == "__main__":
    df = bulten_cek()
    analiz_et(df)

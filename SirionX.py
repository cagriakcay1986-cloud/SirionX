import pandas as pd
import requests
from bs4 import BeautifulSoup

def bulten_cek():
    url = "https://www.iddaa.com/program/canli/futbol"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"}
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # İddaa'nın güncel HTML yapısına göre maçları seç
    maclar = soup.select(".match-name") 
    data = [{"mac": m.text.strip()} for m in maclar]
    
    df = pd.DataFrame(data)
    df.to_csv("maclar.csv", index=False)
    print("Bülten çekildi!")

if __name__ == "__main__":
    bulten_cek()

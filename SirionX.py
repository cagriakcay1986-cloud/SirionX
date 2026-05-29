import pandas as pd
import requests
from bs4 import BeautifulSoup

def bulten_cek():
    url = "https://www.iddaa.com/program/canli/futbol"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    maclar = [{"mac": m.text.strip()} for m in soup.select(".match-name")]
    
    df = pd.DataFrame(maclar)
    df.to_csv("maclar.csv", index=False)
    print("Bülten çekildi ve kaydedildi.")

if __name__ == "__main__":
    bulten_cek()

import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def bulten_cek():

    url = "https://www.iddaa.com/program/canli/futbol"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers, timeout=30)

    soup = BeautifulSoup(response.text, "html.parser")

    maclar = []

    for m in soup.select(".match-name"):

        mac_adi = m.get_text(strip=True)

        analiz = {
            "mac": mac_adi,
            "cekim_tarihi": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "analiz_notu": "Analiz bekleniyor"
        }

        maclar.append(analiz)

    if len(maclar) == 0:
        print("Maç bulunamadı. Site yapısı değişmiş olabilir.")
        return

    df = pd.DataFrame(maclar)

    df.to_csv("maclar.csv", index=False, encoding="utf-8-sig")

    print(f"{len(df)} maç kaydedildi.")

if __name__ == "__main__":
    bulten_cek()

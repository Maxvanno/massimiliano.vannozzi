import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

# Creiamo una lista di date casuali negli ultimi 6 mesi
start_date = datetime.today() - timedelta(days=180)
date_range = [start_date + timedelta(days=np.random.randint(0, 180)) for _ in range(100)]

# Categorie di prodotti e prezzi medi
categorie = ["Elettronica", "Abbigliamento", "Alimentari", "Arredamento", "Sport", "Gioielli"]
prezzi_medi = {"Elettronica": 150, "Abbigliamento": 50, "Alimentari": 20, "Arredamento": 200, "Sport": 80, "Gioielli": 500}

# Generiamo dati casuali
vendite = {
    "Data": [d.strftime("%Y-%m-%d") for d in date_range],
    "Categoria": np.random.choice(categorie, 100),
    "Quantità": np.random.randint(1, 10, 100),
}

# Calcoliamo il prezzo unitario in base alla categoria
vendite["Prezzo Unitario"] = [prezzi_medi[cat] for cat in vendite["Categoria"]]

# Calcoliamo il fatturato
vendite["Fatturato"] = [q * p for q, p in zip(vendite["Quantità"], vendite["Prezzo Unitario"])]

# Creiamo un DataFrame
df_vendite = pd.DataFrame(vendite)

# Salviamo il dataset come CSV
df_vendite.to_csv("dati_vendite.csv", index=False)

print("Dataset 'dati_vendite.csv' creato con successo!")
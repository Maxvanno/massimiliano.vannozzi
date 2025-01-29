import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#caricamento dati
df = pd.read_csv("dati_esempio.csv")

#creazione grafico
plt.figure(figsize=(8,5))
sns.barplot(x="Categoria", y="Valore", data=df, palette="viridis")
plt.title("Analisi delle categorie")
plt.xlabel("Categoria")
plt.ylabel("Valore")

#salvaaggio grafico
plt.savefig("grafico.png")
plt.show()
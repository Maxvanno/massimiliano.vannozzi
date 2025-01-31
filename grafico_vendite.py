import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carichiamo il dataset
df = pd.read_csv("dati_vendite.csv")

# Raggruppiamo il fatturato per categoria
fatturato_categoria = df.groupby("Categoria")["Fatturato"].sum().reset_index()

# Creiamo un grafico a barre
plt.figure(figsize=(10,6))
sns.barplot(x="Fatturato", y="Categoria", data=fatturato_categoria, palette="coolwarm")
plt.xlabel("Fatturato Totale (€)")
plt.ylabel("Categoria di Prodotto")
plt.title("Fatturato Totale per Categoria di Vendita")
plt.grid(axis="x", linestyle="--", alpha=0.7)

# Salviamo il grafico
plt.savefig("grafico_vendite.png")
plt.show()
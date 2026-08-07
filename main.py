import pandas as pd
import plotly.express as px

# Lire le fichier CSV
df = pd.read_csv("ventes.csv")

# Le CSV a été importé sans en-têtes.
# Les vraies colonnes sont dans la première ligne.
df.columns = ["date", "produit", "prix", "qte", "region"]

# Supprimer la première ligne (qui contient les noms des colonnes)
df = df[df["date"] != "date"]

# Convertir les colonnes en nombres
df["prix"] = df["prix"].astype(int)
df["qte"] = df["qte"].astype(int)

# Calculer le chiffre d'affaires
df["chiffre_affaires"] = df["prix"] * df["qte"]

# ==========================
# Graphique 1 : Ventes par produit
# ==========================

ventes = df.groupby("produit")["qte"].sum().reset_index()

fig1 = px.bar(
    ventes,
    x="produit",
    y="qte",
    title="Ventes par produit",
    labels={
        "produit": "Produit",
        "qte": "Quantité vendue"
    }
)

fig1.show()

# ==========================
# Graphique 2 : Chiffre d'affaires par produit
# ==========================

ca = df.groupby("produit")["chiffre_affaires"].sum().reset_index()

fig2 = px.bar(
    ca,
    x="produit",
    y="chiffre_affaires",
    title="Chiffre d'affaires par produit",
    labels={
        "produit": "Produit",
        "chiffre_affaires": "Chiffre d'affaires (€)"
    }
)

fig2.show()

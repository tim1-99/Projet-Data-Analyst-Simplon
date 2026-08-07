--- 07-08-2026 15:32:51 SQLite
---Cette requête calcule le chiffre d'affaires total de l'entreprise 
SELECT SUM(CAST(c3 AS INTEGER) * CAST(c4 AS INTEGER)) AS chiffre_affaires_total
FROM ventes
WHERE c1 <> 'date';
---cette requête calcule la quantité totale vendue de chaque produit 
SELECT c2 AS produit,
       SUM(CAST(c4 AS INTEGER)) AS quantite_vendue
FROM ventes
WHERE c1 <> 'date'
GROUP BY c2;
---cette requête Calcul du chiffre d'affaires par produit
SELECT c2 AS produit,
       SUM(CAST(c3 AS INTEGER) * CAST(c4 AS INTEGER)) AS chiffre_affaires
FROM ventes
WHERE c1 <> 'date'
GROUP BY c2;
---cette requête Calcul des ventes par région
SELECT c5 AS region,
       SUM(CAST(c4 AS INTEGER)) AS quantite_vendue
FROM ventes
WHERE c1 <> 'date'
GROUP BY c5;



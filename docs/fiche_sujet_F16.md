# Fiche sujet F16 — Loi d’Okun

- **Étudiante :** Nave Lehdiya
- **Code Apogée :** 23008668
- **Groupe :** FIN 3
- **Sujet :** Loi d’Okun — Maroc
- **Type de tâche :** Régression linéaire simple
- **Algorithme principal :** Algorithme 1 — Régression linéaire simple
- **Problématique :** Dans quelle mesure la croissance annuelle du PIB réel est-elle associée à la variation annuelle du taux de chômage au Maroc ?
- **Période :** 1992–2024
- **Unité d’observation :** une année pour le Maroc
- **Cible :** `delta_unemployment = unemployment_t - unemployment_(t-1)`, en points de pourcentage
- **Prédicteur :** `gdp_growth`, croissance annuelle du PIB réel, en %
- **Source :** Banque mondiale, World Development Indicators (WDI)
- **Indicateurs :** `NY.GDP.MKTP.KD.ZG` et `SL.UEM.TOTL.ZS`
- **Limite principale :** 33 observations annuelles ; les séries WDI peuvent être révisées.

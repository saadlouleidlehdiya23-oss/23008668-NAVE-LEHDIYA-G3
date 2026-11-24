# Projet Machine Learning — Loi d’Okun au Maroc

**Étudiante :** Nave Lehdiya · **Apogée :** 23008668 · **Groupe :** FIN 3  
**Sujet :** F16 — Loi d’Okun · **Algorithme :** régression linéaire simple (algorithme 1)

## Problématique
Dans quelle mesure la croissance annuelle du PIB réel est-elle associée à la variation annuelle du taux de chômage au Maroc ?

## Résultats principaux du notebook
| Indicateur | Résultat |
|---|---:|
| Période analysée | 1992–2024 |
| Observations | 33 |
| Coefficient de croissance β | -0,102883 |
| Erreur-type HAC (Newey–West, 1 retard) | 0,031379 |
| p-value HAC | 0,002577 |
| R² échantillon complet | 0,401 |
| MAE test chronologique | 0,3911 point |
| RMSE test chronologique | 0,5766 point |
| R² test | 0,4520 |

Le coefficient estimé est négatif et statistiquement significatif avec erreurs-types HAC. Il s’agit d’une association statistique, pas d’une preuve de causalité. Le test chronologique couvre 2015–2024.

## Données
Source : Banque mondiale, World Development Indicators, Maroc :
- Croissance du PIB réel : https://api.worldbank.org/v2/country/MAR/indicator/NY.GDP.MKTP.KD.ZG
- Chômage total : https://api.worldbank.org/v2/country/MAR/indicator/SL.UEM.TOTL.ZS

Les données extraites utilisées sont conservées dans `data/raw/`. Le jeu préparé avec la variation annuelle du chômage est dans `data/processed/`.

## Installation
Python 3.10 ou plus récent :
```bash
pip install -r requirements.txt
```

## Reproduction
1. (Facultatif) Actualiser les données : `python src/telecharger_donnees.py`
2. Ouvrir `notebooks/projet_F16_loi_okun.ipynb`.
3. Exécuter toutes les cellules dans l’ordre. Le notebook interroge l’API World Bank et régénère les tableaux et graphiques.
4. Le rapport LaTeX et son PDF sont dans `rapport/`. Les figures exportées sont dans `figures/`.

## Arborescence
- `data/raw/` : séries sources téléchargées
- `data/processed/` : jeu fusionné et cible dérivée
- `docs/` : fiche F16 et références
- `notebooks/` : notebook exécuté
- `src/` : script de téléchargement
- `figures/` : graphiques du projet
- `rapport/` : rapport LaTeX et PDF
- `presentation/` : diaporama PDF et fichier PowerPoint

## Références et déclaration IA
Voir `docs/references.md` et `DECLARATION_IA.md`.

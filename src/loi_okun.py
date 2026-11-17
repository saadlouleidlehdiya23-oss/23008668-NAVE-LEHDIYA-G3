import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Données du projet
data = {
    'Croissance_economique': [-2, 0, 1, 2, 3, 4, 5, 6, 2.5, 3.5],
    'Taux_chomage': [12, 11, 10.5, 10, 9, 8, 7, 6, 9.5, 8.5]
}

df = pd.DataFrame(data)

# Préparation des données
X = df[['Croissance_economique']]
y = df['Taux_chomage']

# Entraînement du modèle
model = LinearRegression()
model.fit(X, y)

# Prédictions
y_pred = model.predict(X)

# Évaluation
print("Coefficient :", model.coef_[0])
print("Intercept :", model.intercept_)
print("R2 :", r2_score(y, y_pred))

# Graphique
plt.scatter(X, y, label="Données")
plt.plot(X, y_pred, color='red', label="Régression linéaire")
plt.xlabel("Croissance économique (%)")
plt.ylabel("Taux de chômage (%)")
plt.title("Loi d'Okun")
plt.legend()
plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

# Criando um dataframe simulado
np.random.seed(0)
n_samples = 300

# 1. Simulando três features:'feature_1', 'feature_2', 'feature_3'
data = {
    'feature_1': np.random.randn(n_samples) * 2 + 5,
    'feature_2': np.random.randn(n_samples) * 1.5 + 3,
    'feature_3': np.random.randn(n_samples) * 1.2 + 7
}

df = pd.DataFrame(data)

# 2. Pré-processamento dos dados
# DBSCAN é sensível às escalas dos dados, então é comum normalizá-los
scaler = StandardScaler()
X_scaler = scaler.fit_transform(df[['feature_1', 'feature_2']])

# 3. Aplicando o algoritmo DBSCAN
# Definindo os parâmetros de DBSCAN
dbscan = DBSCAN(eps = 0.5, min_samples = 5)
df['cluster'] = dbscan.fit_predict(X_scaler)
df['cluster'].value_counts()

# 4. Visualizando os resultados
plt.scatter(df['feature_1'], df['feature_2'], c = df['cluster'], s = 50, cmap = 'viridis')

# Destacando pontos com ruído (clusters = -1)
plt.scatter(df[df['cluster'] == -1]['feature_1'], df[df['cluster'] == -1]['feature_2'], c = 'red', marker = 'x', s = 100, label = 'Ruído')

plt.title("Clustering com DBSCAN")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.show()
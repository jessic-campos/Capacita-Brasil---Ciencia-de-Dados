# K-Means

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

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

# 2. Aplicando o algoritmo K-means
# Escolhendo duas features para visualização ('feature_1' e 'feature_2')
X = df[['feature_1', 'feature_2']].values

# Definindo o número de clusters (k=3)
kmeans = KMeans(n_clusters = 3)
kmeans.fit(X)

# Prevendo os clusters
df['cluster'] = kmeans.predict(X)

# 3. Visualizando os resultados
plt.scatter(df['feature_1'], df['feature_2'], c = df['cluster'], s = 50, cmap = 'viridis')

# Plotando os centróides
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:,1], c = 'red', s = 200, alpha = 0.75, marker = 'X')

plt.title("Clustering com K-means")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()


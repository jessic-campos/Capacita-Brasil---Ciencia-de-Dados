import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# 1. Geração do Dataset Sintético
np.random.seed(0)
n_samples = 300

data = {
    'valor_medio_gasto': np.random.randn(n_samples) * 20 + 150,
    'frequencia_compras': np.random.randn(n_samples) * 5 + 13,
    'categorias_produtos': np.random.randn(n_samples) * 2 + 7
}

df = pd.DataFrame(data)

# 2. Pré-processamento: Padronização dos dados
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df)

# 3. Método do Cotovelo para determinar número ideal de clusters
plt.figure(figsize=(10, 4))
inertia = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=0, n_init=10)
    kmeans.fit(X_scaled)
    inertia.append(kmeans.inertia_)

plt.plot(range(1, 11), inertia, marker='o', linestyle='--')
plt.xlabel('Número de Clusters (k)')
plt.ylabel('Inércia')
plt.title('Método do Cotovelo para Definir k')
plt.grid(True)
plt.show()

# 4. Aplicando K-means com k=3
kmeans = KMeans(n_clusters=3, random_state=0, n_init=10)
df['cluster'] = kmeans.fit_predict(X_scaled)

# 5. Visualizando apenas o gráfico solicitado
plt.figure(figsize=(10, 6))
scatter = plt.scatter(
    df['frequencia_compras'], 
    df['categorias_produtos'], 
    c=df['cluster'], 
    cmap='viridis', 
    s=70,
    alpha=0.8
)

# Adicionando centróides
centers = scaler.inverse_transform(kmeans.cluster_centers_)
plt.scatter(
    centers[:, 1], 
    centers[:, 2], 
    c='red', 
    s=200, 
    marker='X',
    edgecolor='black',
    label='Centróides'
)

plt.title('Relação entre Frequência de Compras e Diversidade de Produtos')
plt.xlabel('Frequência de Compras')
plt.ylabel('Categorias de Produtos Comprados')
plt.legend()
plt.grid(True)
plt.show()
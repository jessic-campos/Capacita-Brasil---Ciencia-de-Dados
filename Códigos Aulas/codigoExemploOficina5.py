# Importando bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Gerar dados com comportamento linear forte
np.random.seed(0) # Para produzir os resultados
tamanho_imovel = np.random.uniform(50, 200, 100) # Tamanhos em metros
num_quartos = np.random.uniform(2, 6, 100) # Número de quartos

# Definir os coeficientes para uma relação linear forte
coef_tamanho = 1000 # Coeficiente para o tamanho do imóvel
coef_quartos = 5000 # Coeficiente para a quantidade de quartos
intercept = 20000 # Intercept

# Gerar o valor do imóvel com ruído mínimo
valor_imovel = intercept + coef_tamanho * tamanho_imovel + coef_quartos * num_quartos + np.random.normal(0, 1000, 100) # valor com comportamento linear

# Criar Dataframe
df = pd.DataFrame ({
    'tamanho_imovel': tamanho_imovel,
    'num_quartos' : num_quartos,
    'valor_imovel' : valor_imovel,
})

df.head()

# Separando os dados de X e Y
X = df[['tamanho_imovel', 'num_quartos']]
y = df[['valor_imovel']]

# Criando uma regressão  linear
model = LinearRegression()
model.fit(X,y)

# Previsão do valor do imovel com base nos dados de tamanho e número de quartos
previsão = model.predict(X)

# Visualizar o resultado
plt.figure(figsize=(8, 4))
plt.scatter(df['tamanho_imovel'], df['valor_imovel'], label = 'Dados Reais', color = 'b')

# Traçar a reta de regressão
z = np.polyfit(df['tamanho_imovel'], previsão.ravel(), 1)
p = np.poly1d(z)
plt.plot(df['tamanho_imovel'], p(df['tamanho_imovel']), "r--", label = 'Reta de Regressão')

plt.xlabel('Tamanho do Ímovel (m²)')
plt.ylabel('Valor do Imóvel')
plt.title('Regressao Linear')
plt.legend()
plt.show()

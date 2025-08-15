# Importando as biblioteca necessárias
import numpy as np
from tensorflow.keras import models, layers
from tensorflow.keras.dataset import mnist

# Carregando o conjunto de dados do MNIST(digitos manuscritos)
# Ele já está dividido em conjuntos de treino e teste
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Explorando o formato dos dados de treino
print(f"Formatos das imagens de treino: {train_images.shape}")
print(f"Número das imagens de treino: {train_images.shape[0]}")
print(f"Tamanho das imagens de treino: {train_images.shape[1]}x{train_images.shape[2]}")

# Normalizando os dados (os valores dos pixels variam de 0 a 225, vamos ajustar para 0 a 1)
train_images = train_images / 255.0
test_images = test_images / 255.0

# Definindo a arquitetura do modelo
model = models.Sequential()

# A camada Flatten achata a imagem 28x28 em um vetor de 784 elementos (28x28)
model.add(layers.Flatten(input_shape = (28,28)))

# Camada densa com 128 neurônios e ativação ReLu 
model.add(layers.Dense(128, activation = 'relu'))

# Camada de saída com 10 neurônios (para as 10 classes de dígitos) e ativação softwax
model.add(layers.Dense(10, activation = 'softmax'))

# Resumo da arquitetura do modelo
model.summary()

# Compilando o modelo
# Utilizamos o otimizador Adam, a função de perda para classificação categórica e a métrica de acurácia
model.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])

#
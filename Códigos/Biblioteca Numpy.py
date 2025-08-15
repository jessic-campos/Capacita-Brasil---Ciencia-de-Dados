import numpy as np
import pandas as pd

lista =  [12, 45, 67, 23, 89, 34, 22, 90, 56, 78]

###Calculo da média da lista:
media = np.mean(lista)
print("Média:", media)

###Identificando os números maiores que a média:
vetor = np.array(lista) #Transformei em vetor para aproveitar a biblioteca numpy no lugar de usar for
maiores = vetor[media < vetor]
print("Maiores:", maiores)

###Guardando no DataFrame
vetorM = pd.DataFrame(maiores)
print(vetorM)

###Salvando em CSV
vetorM.to_csv("numeros_maiores_que_media.csv", index = False)
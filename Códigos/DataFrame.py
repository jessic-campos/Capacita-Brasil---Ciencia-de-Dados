import pandas as pd
import numpy as np

#### Crie um DataFrame com base nos dados fornecidos
dados = {
    'Nome': ['Ana', 'Bruno', 'Carlos', 'Daniela', 'Eduardo'],

    'Idade': [28, 34, 29, None, 42],

    'Cidade': ['São Paulo', 'Rio de Janeiro', None, 'Curitiba', 'Belo Horizonte'],

    'Vendas': [150, 200, 300, 400, None]
}

df = pd.DataFrame(dados)

#### Filtre os clientes que têm mais de 30 anos
acima30 = df[df["Idade"] > 30]
print(acima30, "\n")

#### Calcule a média de idade dos clientes
media = df["Idade"].mean()
print("Media das idade:", media, "\n")

#### Substitua valores faltantes na coluna Cidade por ‘Desconhecido’
df["Cidade"] = df["Cidade"].fillna("Desconhecido")
print(df, "\n")

#### Calcule a soma total das vendas
soma = df["Vendas"].sum()
print("Soma das vendas:", soma, "\n")




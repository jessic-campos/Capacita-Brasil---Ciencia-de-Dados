from functools import reduce

def soma(x, y):
    return x + y

numeros = [1, 2, 3, 4, 5]

resultado = reduce(soma, numeros)

print(resultado)  # Saída: 15

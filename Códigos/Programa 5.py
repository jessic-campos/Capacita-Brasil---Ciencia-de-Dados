# Escreva um código usando enumerate para exibir os indices e valores da lista ["maçã", "banana", "uva"]

frutas = ["maçã", "banana", "uva"]

for indice, fruta in enumerate(frutas):
    print(f"{indice}: {fruta}")


# Crie uma lista com os numeros pares de 1 a 10 usando List Comprehension

numeros = [x for x in range(1, 11) if x % 2 == 0]
print(numeros)


#Escreva um programa que use map para multiplicar cada elemento da lista [1, 2, 3, 4] por 3.

lista = [1, 2, 3, 4]
resultado = map(lambda x: x* 3, lista)

#1 * 3 = 3
#2 * 3 = 6
#3 * 3 = 9
#4 * 3 = 12

print(list(resultado))


# Escreva um programa que use enumerate e List Comprehension para criar uma lista de tuplas com os índices e valores ao quadrado de [2, 4, 6]

numeros2 = [2, 4, 6]
resultado = [(indice, valor ** 2) for indice, valor in enumerate(numeros2)]

print(resultado)

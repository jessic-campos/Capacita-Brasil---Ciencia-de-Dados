
# Crie um programa que use um laço for para imprimir os números de 1 a 5 no console.
print()
for i in range(5):
    print(i + 1)
print()
    

# Escreva um programa que declare uma lista com os números [10, 20, 30, 40, 50] e exiba o primeiro elemento.

lista = [10, 20, 30, 40, 50]
print(lista[0])
print()

# Faça um programa que use um laço while para somar todos os números de 1 a 10 e exiba o resultado no console.

contador = 1
soma = 0

while contador <= 10:
    soma = contador + soma;
    contador =  contador + 1;

# 0 + 1
# 1 + 2 
# 3 + 3
# 6 + 4
# 10 + 5
# 15 + 6
# 21 + 7
# 28 + 8
# 36 + 9 
# 45 + 10
print(soma)
print()

# Crie um programa que declare um dicionário com as seguintes chaves e valores: {"nome": "Ana", "idade": 25, "cidade": "Fortaleza"}
# e exiba o valor associado à chave "idade"

pessoa = {"nome": "Ana", "idade": 25, "cidade": "Fortaleza"}
print(pessoa["idade"]) #multiplos argumentos, achei mais simples
#print(pessoa.get("idade")) #usando get para tornar idade, caso não existisse a chave correspondente seria imprimido none
print()

# Escreva um programa que inverta uma string utilizando um laço for. Por exemplo, para a string "Python", o resultado deve ser "nohtyP".

texto = "Python"
texto_invertido = ""
for i in range(len(texto) - 1, -1, -1):
    texto_invertido += texto[i]
print(texto_invertido)
print()

# Escreva um programa que calcule a frequência de cada caractere em uma string. 
# Por exemplo, na string "banana", o programa deve exibir: {'b': 1, 'a': 3, 'n': 2}

palavra = input()

frequencia = {}

for i in palavra:
    if i in frequencia:
        frequencia[i] += 1 # se a letra já tiver sido adicionada então conta a aparição
    else:
        frequencia[i] = 1 # se não adiciona

print(f"{frequencia}")
print()
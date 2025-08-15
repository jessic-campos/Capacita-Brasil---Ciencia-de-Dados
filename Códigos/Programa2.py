#Crie um programa que verifique se o número 15 é maior que 10 e exiba "Sim" ou "Não" no console.

if 15 > 10:
    print("Sim")
else:
    print("Não")

#Escreva um programa que use o operador ** para calcular 2³ e exiba o resultado.

print(2**3)

#Crie um programa que use o operador * para repetir a string "Oi!" cinco vezes.

print(5*"Oi")

#Escreva um programa que calcule a média de três números inteiros 10, 20 e 30, 
# e exiba no console se a média é maior, menor ou igual a 20.

media = (10 + 20 + 30)/3

if media > 20:
    print("Média é maior que 20")
elif media == 20:
    print("Média é igual a 20")
else:
    print("Média é menor que 20")

#Crie um programa que determine se o número 45 é divisível por 3 e por 5 simultaneamente. 
# O programa deve exibir "Divisível por 3 e 5" ou "Não é divisível.

if(45%3 == 0 and 45%5 == 0):
    print("Divisível por 3 e 5")
else:
    print("Não é divisível")
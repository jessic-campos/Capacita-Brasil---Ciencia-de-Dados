contador = 0
num = 1
soma_par = 0
soma_impar = 0

while num != 0:
    num = int(input("Digite um número: "))
    if(num%2 == 0):
        soma_par = num + soma_par
    else:
        soma_impar = num + soma_impar
    

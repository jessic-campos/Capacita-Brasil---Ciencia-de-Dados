
"""Usando esse exemplo poderia ser obtido o resultado sem a necessidade de usar diretamente 
a variável booleana apenas atráves das estruturas condicionais, mas também é possível o uso
do true e false ao implementar uma variável auxiliar.
"""
num = int(input("Digite o número para verificar se é par: "))


if num%2 == 0:
    verificar = True
else:
    verificar = False

print(verificar) #Aqui será imprimido True quando for par e false para os outros casos

repeti = 3*"Oi"
print(repeti)
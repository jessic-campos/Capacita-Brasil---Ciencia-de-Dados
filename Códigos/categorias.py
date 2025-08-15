idade = int(input("Digite a idade do atleta: "))

if idade < 12:
    print("Sua categoria é a infantil")
elif 12 >= idade and idade < 18:
    print("Sua categoria é a juvenil")
else:
    print("Sua categoria é a adulto")
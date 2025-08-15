
areaPintada = int(input("Qual o tamanho da área a ser pintada:"))

litros = areaPintada/3
latas = 1 + litros / 18
valor = latas * 80

print(f"A quantidade de latas foi {latas:.2f} e o valor foi {valor:.2f}")

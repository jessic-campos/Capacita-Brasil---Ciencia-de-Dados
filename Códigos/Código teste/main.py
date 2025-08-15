import distancia

xa = float(input("Digite o ponto Xa: "))
ya = float(input("Digite o ponto Ya: "))
xb = float(input("Digite o ponto Xb: "))
yb = float(input("Digite o ponto Yb: "))

# Cálculo e saída
resultado = distancia.distancia(xa, ya, xb, yb)
print(f"{resultado:.2f}")

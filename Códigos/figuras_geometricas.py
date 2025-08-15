# Uma função para calcular a área de um quadrado e outra função para calcular a área de um retângulo.

def quadrado(lados):
    area = lados * lados
    return area

def retangulo(base, altura):
    area = base * altura
    return area

# main

quadrado_lado = int(input("Digite o tamanho de um lado do quadrado: "))
area_quadrado = quadrado(quadrado_lado)

base = int(input("Digite a base do retângulo: "))
altura = int(input("Digite a altura do retangulo: "))
area_retangulo = retangulo(base, altura)

print(f"{area_quadrado}")
print(f"{area_retangulo}")

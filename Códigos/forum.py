senha = 25831
desbloqueio = 0
contador = 0

while desbloqueio != senha:
    desbloqueio = (input("Digite sua senha: "))
    contador += 1
    
    if contador == 15:
        print("Você errou a senha 15 vezes, seu celular será restaurado ao estado de fábrica")
        break

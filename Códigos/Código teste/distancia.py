import math

def distancia(xa, ya, xb, yb):

    ponto_x = xb - xa
    ponto_y = yb - ya

    potencia_final = math.pow(ponto_x, 2) + pow(ponto_y, 2)
    distancia = math.sqrt(potencia_final)

    return distancia






import pygame
import sys
import random

# Inicialização
pygame.init()
largura, altura = 600, 400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo da Cobrinha")
relogio = pygame.time.Clock()

# Cores
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)

# Variáveis da cobrinha
tamanho_bloco = 20
cobra = [(100, 100)]
direcao = (tamanho_bloco, 0)

# Maçã
def nova_maca():
    return (random.randint(0, (largura - tamanho_bloco) // tamanho_bloco) * tamanho_bloco,
            random.randint(0, (altura - tamanho_bloco) // tamanho_bloco) * tamanho_bloco)

maca = nova_maca()

def desenhar():
    tela.fill(PRETO)
    for parte in cobra:
        pygame.draw.rect(tela, VERDE, (*parte, tamanho_bloco, tamanho_bloco))
    pygame.draw.rect(tela, VERMELHO, (*maca, tamanho_bloco, tamanho_bloco))
    pygame.display.flip()

def mover_cobra():
    global maca
    nova_cabeca = (cobra[0][0] + direcao[0], cobra[0][1] + direcao[1])
    cobra.insert(0, nova_cabeca)
    if nova_cabeca == maca:
        maca = nova_maca()
    else:
        cobra.pop()

def verificar_colisoes():
    x, y = cobra[0]
    if (x < 0 or x >= largura or y < 0 or y >= altura or cobra[0] in cobra[1:]):
        return True
    return False

# Loop principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP and direcao != (0, tamanho_bloco):
                direcao = (0, -tamanho_bloco)
            elif evento.key == pygame.K_DOWN and direcao != (0, -tamanho_bloco):
                direcao = (0, tamanho_bloco)
            elif evento.key == pygame.K_LEFT and direcao != (tamanho_bloco, 0):
                direcao = (-tamanho_bloco, 0)
            elif evento.key == pygame.K_RIGHT and direcao != (-tamanho_bloco, 0):
                direcao = (tamanho_bloco, 0)

    mover_cobra()
    if verificar_colisoes():
        break
    desenhar()
    relogio.tick(2)

pygame.quit()


import pygame
import sys
import math

# Inicializa o Pygame
pygame.init()

# Tamanho da janela
largura = 500
altura = 500
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Pac-Man Ricochete Direcionado")

# Cores
AZUL = (12, 10, 40)
AMARELO = (255, 255, 0)

# Configurações do Pac-Man
pacman_x = 250
pacman_y = 250
vel_x = 0
vel_y = 0
velocidade = 5
tamanho = 40  # raio

clock = pygame.time.Clock()

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Verifica teclas pressionadas (muda direção)
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        vel_x = -velocidade
        vel_y = 0
    if teclas[pygame.K_RIGHT]:
        vel_x = velocidade
        vel_y = 0
    if teclas[pygame.K_UP]:
        vel_y = -velocidade
        vel_x = 0
    if teclas[pygame.K_DOWN]:
        vel_y = velocidade
        vel_x = 0

    # Atualiza posição
    pacman_x += vel_x
    pacman_y += vel_y

    # Ricochete horizontal
    if pacman_x - tamanho <= 0 or pacman_x + tamanho >= largura:
        vel_x = -vel_x

    # Ricochete vertical
    if pacman_y - tamanho <= 0 or pacman_y + tamanho >= altura:
        vel_y = -vel_y

    # Desenha fundo
    janela.fill(AZUL)

    # Desenha o corpo do Pac-Man
    pygame.draw.circle(janela, AMARELO, (pacman_x, pacman_y), tamanho)

    # Atualiza tela
    pygame.display.update()
    clock.tick(60)

# Encerra o Pygame
pygame.quit()
sys.exit()

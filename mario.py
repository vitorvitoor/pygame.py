import pygame
import os
import time
import random

pygame.init()


def limparTela():
    os.system("cls")


limparTela()
print("Jogo do mario")

largura = 600
altura = 428
tamanho = (largura, altura)
branco = (255, 255, 255)
display = pygame.display.set_mode(tamanho)
fps = pygame.time.Clock()
gameEvents = pygame.event

mario = pygame.image.load("assets/mario.png")
fundo = pygame.image.load("assets/fundoMario.jpg")
pygame.display.set_caption("SUPER MARIO DOS GURI")

jogando = True
posicaoMarioX = 400
posicaoMarioY = 255

marioAltura = 93
marioLargura = 93
movimentoMarioX = 0

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                movimentoMarioX = -5
            elif evento.key == pygame.K_RIGHT:
                movimentoMarioX = 5
        elif evento.type == pygame.KEYUP:
            movimentoMarioX = 0

    posicaoMarioX = posicaoMarioX + movimentoMarioX         
    display.fill(branco)
    posicao = (posicaoMarioX, posicaoMarioY)
    display.blit(fundo, (0, 0))
    display.blit(mario, posicao)

    pygame.display.update()
    fps.tick(144)

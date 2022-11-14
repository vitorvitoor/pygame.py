import pygame
import random
import time
pygame.init()
pygame_display = pygame.display
pygame_display.set_caption('Super Mario')
altura = 0
largura = 0
tamanho = (altura, largura)
game_display = pygame.display.set_mode(tamanho)
clock = pygame.time.Clock()
game_events = pygame.event
branco = (255,255,255)
fundo = pygame.image.load('assets/fundo.jpg')

def escrever_texto(texto):
    fonte = pygame.font.Font('freesansbold.ttf', 15)
    texto_display = fonte.render(texto,True,branco)
    game_display.blit(texto_display, (880,80))
    pygame_display.update()


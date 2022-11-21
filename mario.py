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
vermelho = (255, 0, 0)
display = pygame.display.set_mode(tamanho)
fps = pygame.time.Clock()
gameEvents = pygame.event
pygameDisplay = pygame.display

mario = pygame.image.load("assets/mariopng.png")
fundo = pygame.image.load("assets/fundoMario.jpg")
coin = pygame.image.load("assets/pngegg.png")
pygame.display.set_caption("SUPER MARIO DOS GURI")

def escrever(texto):
    fonte = pygame.font.Font("freesansbold.ttf", 25)
    textoDisplay = fonte.render(texto,True,(0,0,0))
    display.blit(textoDisplay, (450,60))
    pygameDisplay.update()

def morreu():
    fonte = pygame.font.Font("freesansbold.ttf", 35)
    fonte2 = pygame.font.Font("freesansbold.ttf", 35)
    fonte3 = pygame.font.Font("freesansbold.ttf", 30)
    textoDisplay = fonte.render("FALICEUUUU!!!!", True, vermelho)
    textoDisplay2 = fonte2.render("Pressione ENTER para continuar!", True, (0,0,0))
    textoDisplay3 = fonte2.render("Pressione ENTER para continuar!", True, (0,255,255))
    display.blit(textoDisplay,(160,110))
    display.blit(textoDisplay2, (14,150))
    display.blit(textoDisplay3, (15,151))
    pygameDisplay.update()

def jogar():
    jogando = True
    posicaoMarioX = 400
    posicaoMarioY = 297
    marioAltura = 93
    marioLargura = 80
    movimentoMarioX = 0
    eggLargura = 50
    eggAltura = 50
    posicaoEggX = 200
    posicaoEggY = 200
    velocidadeEgg = 2
    pontos = 0
    pygame.mixer.music.load("assets/marioMusica.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(-1)
    
    derrotaMario = pygame.mixer.Sound("assets/marioDerrota.mp3")
    derrotaMario.set_volume(1)
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit(),
                jogando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    movimentoMarioX = -5
                elif evento.key == pygame.K_RIGHT:
                    movimentoMarioX = 5
                elif evento.key == pygame.K_RETURN:
                    jogar()
            elif evento.type == pygame.KEYUP:
                movimentoMarioX = 0
            if posicaoMarioX + movimentoMarioX < 520 and posicaoMarioX + movimentoMarioX > -30:
                posicaoMarioX = posicaoMarioX + movimentoMarioX 
    
        if jogando:
            if posicaoEggY > altura:
                posicaoEggY = -240
                posicaoEggX = random.randint(10, 590)
                pontos = pontos + 1
            else:
                posicaoEggY = posicaoEggY + velocidadeEgg

            if posicaoMarioX + movimentoMarioX > 0 and posicaoMarioX + movimentoMarioX < largura - marioLargura:
                posicaoMarioX = posicaoMarioX + movimentoMarioX
            display.fill(branco)
            posicao = (posicaoMarioX, posicaoMarioY)
            display.blit(fundo, (0, 0))
            display.blit(mario, (posicaoMarioX, posicaoMarioY))
            display.blit(coin, (posicaoEggX, posicaoEggY))
            escrever("Pontos: " + str(pontos))

            corpoMarioX = list(range(posicaoMarioX, posicaoMarioX + marioLargura))
            corpoMarioY = list(range(posicaoMarioY, posicaoMarioY + marioAltura))

            corpoEggX = list(range(posicaoEggX, posicaoEggX + eggLargura))
            corpoEggY = list(range(posicaoEggY, posicaoEggY + eggAltura))
        
            colisaoY = len(list(set(corpoEggY) & set(corpoMarioY) ))
            if colisaoY > 44:
                colisaoX = len(list(set(corpoEggX) & set(corpoMarioX) ))
                print(colisaoX)
                if colisaoX > 30 :
                    morreu()
                    jogando = False
                    pygame.mixer.music.stop()
                    pygame.mixer.Sound.play(derrotaMario)


        pygame.display.update()
        fps.tick(144)

jogar()
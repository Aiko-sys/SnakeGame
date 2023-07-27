import pygame
from pygame.locals import *
from sys import exit


pygame.init()
altura = 630
largura= 1000
x_rect= largura/2
y_rect= altura/2
from random import randint

xcontr = 20
ycontr = 0
tick = 16
pontos = 0


font = pygame.font.SysFont('arial', 40, True, False)
font_game_over =pygame.font.SysFont('arial', 80, True, False)
font_game_over_msg =pygame.font.SysFont('arial', 30, True, False)


x_circl = randint(10, largura)
y_circl = randint(10, altura)
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Snake Game')
comprimento_cobra = 3
lista_toda = []
def Corpo(lista_toda):
    for xy in lista_toda:
        
        pygame.draw.rect(tela, (0, 179, 0), (xy[0],xy[1],20,20))


title = pygame.mixer.music.load("songs/Title.mp3")
pygame.mixer.music.play(-1)
Point = pygame.mixer.Sound("songs/Point.wav")
clock = pygame.time.Clock()
death = False
def restart():
    global pontos, x_rect, y_rect, lista_toda, Lista_cbc, death, x_circl, y_circl, tick, comprimento_cobra 
    pontos = 0
    comprimento_cobra = 3
    x_rect = largura/2
    y_rect= altura/2
    tick = 16
    Lista_cbc = []
    lista_toda = []
    x_circl = randint(10, largura)
    y_circl = randint(10, altura)
    death = False

while not death:

    game_over = f'Game Over'
    game_over_msg = f'press SPACE to Restart'   
    msg = f'Score : {pontos}'
    clock.tick(tick)
    tela.fill((255, 255, 255))
    formated_game_over = font_game_over.render(game_over, True, (0, 0, 0))
    formated_game_over_msg = font_game_over_msg.render(game_over_msg, True, (255, 0, 0))
    formated = font.render(msg, False, (0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
            
        if event.type == KEYDOWN:
            if ycontr != 20:
                if event.key == K_w:
                    xcontr=0
                    ycontr=-20
            if xcontr != -20:
                if event.key == K_d:
                    xcontr=20
                    ycontr=0
            if ycontr != -20:
                if event.key == K_s: 
                    xcontr=0
                    ycontr=20
            if xcontr != 20:
                if event.key == K_a: 
                    xcontr=-20
                    ycontr=0

    x_rect += xcontr
    y_rect += ycontr
    cobrinha = pygame.draw.rect(tela, (0, 179, 0), (x_rect,y_rect,20,20))
    fruta = pygame.draw.circle(tela, (255, 5, 0), (x_circl, y_circl), (15))
    if cobrinha.colliderect(fruta):
        x_circl = randint(1, largura)
        y_circl = randint(1, altura)
        pontos +=1
        comprimento_cobra+=1
        Point.play()
        tick+=0.2
    
    
    Lista_cbc = []
    Lista_cbc.append(x_rect)
    Lista_cbc.append(y_rect)
    lista_toda.append(Lista_cbc)
    Corpo(lista_toda)

    if lista_toda.count(Lista_cbc) > 1:
        death = True
        while death:
            tela.fill((255, 255, 255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        restart()
            tela.blit(formated_game_over, (320, altura/2-130))
            tela.blit(formated_game_over_msg, (355, altura/2-40))
            pygame.display.update()
    if x_rect > largura:
        x_rect = 0
    elif x_rect < 0:
        x_rect = largura    
    if y_rect > altura:
        y_rect = 0
    elif y_rect < 0:
        y_rect = altura



    if len(lista_toda) > comprimento_cobra:
            del lista_toda[0]
    tela.blit(formated, (800, 50))
    pygame.display.update()
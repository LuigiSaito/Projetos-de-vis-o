import pygame
import time
import random

azul = (0,0,255) #define o RGB das cores da cobrinha
vermelho = (255,0,0)
preto = (0,0,0)
verde = (0,255,0)
branco = (255,255,255)

display_width = 800
display_height = 600

pygame.init()
display = pygame.display.set_mode((display_width , display_height)) #cria um display grafico om dimenções de 800x600
pygame.display.set_caption("Jogo da cobrinha")#cria um titulo para o dislplay


#Criaremos agora um loop, que mantem o display aberto enquanto o jogo não for perdido, ou seja
#enquando a avariavel game_over for falso

game_over = False #fim de jogo? -> não por enquanto

#adiciona movimento a cobra
x_init= display_width/2 #coord x inicial
y_init = display_height/2 #coord y inicial

snake_block = 10 #o quanto o bloco muda
snake_speed = 15

snake_List = [] #dados da cobra guarda o tamanho da mesam
Length_of_snake = 1 #tamanho inicial da cobra

x1_change = 0 #variavel de mudança de posição
y1_change = 0

foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0 #adiciona comida no jogo
foody = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0

clock = pygame.time.Clock() #tempo no jogo, cria um relogio


font_style = pygame.font.SysFont("Segoe UI", 35)
def our_snake(snake_block, snake_list): #função que cria a cobra
    for x in snake_list:
        pygame.draw.rect(display, verde, [x[0], x[1], snake_block, snake_block])

def message(msg, color, altura, largura): #define a função que escreve a mensagem na tela
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [altura, largura])

while(game_over != True):
    for event in pygame.event.get(): #capta todos os dados do teclado/mouse
        if event.type == pygame.QUIT: #caso o jogo for fechado, game_over -> vdd logo fecha a janela
            game_over = True #muda a constante de estado de jogo para desligada
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a: #movimento da cobra, quanto ela semexe a cada clique
                x1_change = -snake_block
                y1_change = 0
            elif event.key == pygame.K_d:
                x1_change = snake_block
                y1_change = 0
            elif event.key == pygame.K_w:
                x1_change = 0
                y1_change = -snake_block
            elif event.key == pygame.K_s:
                x1_change = 0
                y1_change = snake_block

    if x_init >= display_width or x_init < 0 or y_init >= display_height or y_init < 0:
        # caso a cobra bata na borda ou nela mesma o jogo acaba
        game_over = True

    x_init += x1_change #faz a da mudança no valor inicial
    y_init += y1_change
    display.fill(preto)
    pygame.draw.rect(display, vermelho, [foodx, foody, snake_block, snake_block]) #adiciona comidas ao mapa
    snake_Head = []
    snake_Head.append(x_init)
    snake_Head.append(y_init)
    snake_List.append(snake_Head)
    if len(snake_List) > Length_of_snake:
        del snake_List[0]
    for x in snake_List[:-1]: #se ela bater nela emsam ela morre
        if x == snake_Head:
            game_over = True
    our_snake(snake_block, snake_List)

    pygame.display.update()

    if x_init == foodx and y_init == foody: #cria a fisica de pegar a comida
        foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0
        Length_of_snake += 1
        snake_speed += 1


    clock.tick(snake_speed)
message("Voce perdeu :C",vermelho,300, display_height / 2)
message(f"Seu score foi de: {Length_of_snake - 1}",branco,260, 80)
pygame.display.update()
time.sleep(2)

pygame.quit() #sai do display
quit()


"""SAlva os dados da cobra como se fosse uma lista, que vai aumentando"""
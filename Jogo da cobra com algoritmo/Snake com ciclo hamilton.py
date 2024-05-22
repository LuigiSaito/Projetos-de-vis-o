import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
cinza  = (220, 220, 220)

dis_width = 400
dis_height = 400

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game com ia')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 50

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])


def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    posi = dis_height / 2
    aux = 0
    gambi = 0
    helpi = 0
    marinha = 0

    snake_List = []
    Length_of_snake = 100

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
        x1_change = 0
        y1_change = 0
        #fazer 2 desse com ajuda da variavel helpi, se ela for 0 vai até 380 se for 1 vai até 390
        if helpi < dis_height/10 or helpi == 0:
            if (x1 <= dis_width - 2*snake_block and aux == 0):
                x1_change = snake_block
                #print('passo 1')

            if (x1 == dis_width - 2*snake_block):
                y1_change = -snake_block
                aux = 1

            if aux == 1 and x1 > 0 and x1 <= 400:
                x1_change = -snake_block

            if (x1 == 0):
                y1_change = -snake_block
                x1 += snake_block
                aux = 0
            if x1 == dis_width - 2*snake_block and y1 == 0:
                x1_change = snake_block
                x1 = dis_height - snake_block
                y1_change = 0
                gambi += 1

            if gambi > 0 and y1 <= 400:
                x1_change = 0
                y1_change = snake_block
                helpi += 1
                #print(helpi)
            if y1 == 0 and x1 == 0:
                y1_change = snake_block

            #print(f'em y: {y1}')
            #print(f'em x: {x1}')
        if helpi >= dis_height/10:
            if y1 == dis_width - snake_block:
                x1_change = -snake_block
                y1_change = 0
                #print('passo 4')
            if x1 == 0:
                y1_change = -snake_block
                x1_change = snake_block
                helpi = 0
                aux = 0
                gambi = 0
            #print(f'em y: {y1}')
            #print(f'em x: {x1}')




        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
            print('faio')
        x1 += x1_change
        y1 += y1_change
        dis.fill(cinza)
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()
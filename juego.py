#Autor: Jose Galarza

import pygame
from random import randint, sample
from buscaMina import BuscaMina

pygame.init()

size = WIDTH , HEIGTH = 300, 300

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

font = pygame.font.Font('freesansbold.ttf', 10)


state_screen = True
button_pos = (-1,-1)
mouse_x = -1
mouse_y = -1

Juego = BuscaMina()

while state_screen:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            state_screen = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x = event.pos[1]
            mouse_y = event.pos[0]


    screen.fill(BLACK)

    Juego.draw_Mapa(screen)

    if (mouse_x != -1 and mouse_y != -1):
        Juego.update_Cuadro(mouse_x,mouse_y,screen)
        mouse_x = -1
        mouse_y = -1

    Juego.draw_minas_cuadro(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
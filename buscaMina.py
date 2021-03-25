#Autor: Jose Galarza

import pygame
from random import sample, randint
from math import floor


WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GRAY = (40, 116, 166)

class BuscaMina():

    def __init__(self):
        self.mapa = [[ False for _ in range(20) ] for _ in range (20)]
        self.numMinas = 20
        self.minas_cuadro = []

        self.insertMinas(self.numMinas)

    def insertMinas(self, numMinas):
        element = 0
        minas = []
        num_minas = numMinas
        while element < num_minas:
            if element == 0:
                minas.append([randint(0,19),randint(0,19)])
                element=len(minas)
            else:
                x=randint(0,19)
                y=randint(0,19)
                state = True
                for mina in minas:
                    if mina == [x,y]:
                        state = False

                if state:
                    minas.append([x,y])

            element=len(minas)           

        for i in minas:
            self.mapa[i[0]][i[1]] = True


    def draw_Mapa(self,screen):
        for x in range(len(self.mapa)):
            for y in range(len(self.mapa)):
                pygame.draw.rect(screen,WHITE,[x*15,y*15,15,15])
                pygame.draw.rect(screen,GRAY,[x*15,y*15,15,15],3)

    def update_Cuadro(self,mouse_x, mouse_y,screen):
        x = floor(mouse_x/15)
        y = floor(mouse_y/15)

        self.verificar_mina(x,y,screen)

    def verificar_mina(self,x,y,screen):
        minas_alrededor = 0
        if( not self.mapa[x][y] ):
            for i in range(x-1,x+2):
                for j in range(y-1,y+2):
                    if (self.validar_posiciones(i,j)):
                        if(self.mapa[i][j]):
                            minas_alrededor += 1
            self.num_minas_cuadro(minas_alrededor,x,y)

        else:
            self.lose_game(screen)
        
        if (minas_alrededor == 0):
            count_extrem = 0
            if( not self.mapa[x][y] ):
                for i in range(x-1,x+2):
                    for j in range(y-1,y+2):
                        if (self.validar_posiciones(i,j)):
                            for k in range(i-1,i+2):
                                for l in range(j-1,j+2):
                                    if (self.validar_posiciones(k,l)):
                                        if(self.mapa[k][l]):
                                            count_extrem += 1
            if count_extrem == 0:
                for i in range(x-1,x+2):
                    for j in range(y-1,y+2):
                        if (self.validar_posiciones(i,j)):
                            self.num_minas_cuadro(minas_alrededor,i,j)


    def validar_posiciones(self,x,y):
        if( x == -1):
            return False
        if ( y == -1):
            return False
        if ( x == 20):
            return False
        if ( y == 20 ):
            return False
        return True

    def num_minas_cuadro(self, minas_alrededor, x, y):
        font = pygame.font.Font('freesansbold.ttf',12)
        minas_text = str(minas_alrededor)
        OUT = font.render(minas_text,False, BLACK)
        self.minas_cuadro.append([x,y,OUT])

    def draw_minas_cuadro(self,screen):
        for x in self.minas_cuadro:
            screen.blit(x[2],(x[1]*15+4, x[0]*15+2))

    def lose_game(self,screen):
        font = pygame.font.Font('freesansbold.ttf',40)
        lose_text = "PERDISTE"
        OUT = font.render(lose_text,False, RED)
        screen.blit(OUT,(50,100))
        pygame.display.flip()
        pygame.time.wait(1000)
        self.mapa = [[ False for _ in range(20) ] for _ in range (20)]
        self.minas_cuadro = []
        self.insertMinas(self.numMinas)
import pygame as pg
import random

ANCHO = 500
ALTO = 500
SIZE = (ANCHO, ALTO)

BLACK = (0,0,0)
RED = (255,0,0)
VERDE = (0,255,0)
AZUL = (0,0,255)

if __name__=="__main__":
    pg.init()
    ventana = pg.display.set_mode(SIZE)
    pg.display.set_caption("Naves")



    stop = False
    while stop == False:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                stop = True
                

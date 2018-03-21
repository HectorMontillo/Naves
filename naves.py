import pygame as pg
import random

#CONSTANTES
ANCHO = 1000
ALTO = 500
SIZE = (ANCHO, ALTO)

BLACK = (0,0,0)
RED = (255,0,0)
VERDE = (0,255,0)
AZUL = (0,0,255)

#CLASES
class Nave(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((20,20))
        self.image.fill(AZUL)
        self.rect = self.image.get_rect()
        self.rect.left = 32
        self.rect.centery = ALTO/2



if __name__=="__main__":

    #INICIALIZAR
    pg.init()
    ventana = pg.display.set_mode(SIZE)
    pg.display.set_caption("Naves")

    #CARGAR IMAGENES


    #CREAR GRUPOS
    TODOS = pg.sprite.Group()
    PLAYERS = pg.sprite.Group()

    #CREAR OBJETOS
    nave = Nave()
    PLAYERS.add(nave)
    TODOS.add(nave)




    #CICLO PRINCIPAL
    stop = False
    while stop == False:
        #EVENTOS
        for event in pg.event.get():
            if event.type == pg.QUIT:
                stop = True

        #ACTUALIZAR
        TODOS.update()

        #RENDERIZAR
        ventana.fill(BLACK)
        TODOS.draw(ventana)

        #FLIP
        pg.display.flip()

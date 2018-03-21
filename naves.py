import pygame as pg
import random

#CONSTANTES
ANCHO = 1000
ALTO = 500
SIZE = (ANCHO, ALTO)
FPS = 60

BLACK = (0,0,0)
RED = (255,0,0)
VERDE = (0,255,0)
AZUL = (0,0,255)
AMARILLO = (255,255,0)

#CLASES
class Nave(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((32,32))
        self.image.fill(AZUL)
        self.rect = self.image.get_rect()
        self.rect.left = 32
        self.rect.centery = ALTO/2
        self.velx = 0
        self.vely = 0
        self.vel = 5


    def update(self):
        #self.rect.center = pg.mouse.get_pos()
        self.velx = 0
        self.vely = 0
        keystate = pg.key.get_pressed()

        if keystate[pg.K_SPACE]:
            self.vel = 10
        else:
            self.vel = 5

        if keystate[pg.K_LEFT] or keystate[pg.K_a]:
            self.velx = -self.vel
        if keystate[pg.K_RIGHT] or keystate[pg.K_d]:
            self.velx = self.vel
        self.rect.x += self.velx

        if keystate[pg.K_UP] or keystate[pg.K_w]:
            self.vely = -self.vel
        if keystate[pg.K_DOWN] or keystate[pg.K_s]:
            self.vely = self.vel
        self.rect.y += self.vely

        if self.rect.right > ANCHO:
            self.rect.right = ANCHO
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > ALTO:
            self.rect.bottom = ALTO
        if self.rect.top < 0:
            self.rect.top = 0

    def disparar(self):
        bala = Bala(self.rect.center)
        BALAS.add(bala)
        TODOS.add(bala)

class Mira(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((8,8))
        self.image.fill(VERDE)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = pg.mouse.get_pos()



class Bala(pg.sprite.Sprite):
    def __init__(self,xy):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((8,8))
        self.image.fill(AMARILLO)
        self.rect = self.image.get_rect()
        self.rect.center = xy
        self.vel = 10

    def update(self):
        self.rect.x += self.vel

        if self.rect.left > ANCHO:
            self.kill()



if __name__=="__main__":

    #INICIALIZAR
    pg.init()
    ventana = pg.display.set_mode(SIZE)
    pg.display.set_caption("Naves")
    pg.mouse.set_visible(False)
    reloj = pg.time.Clock()

    #CARGAR IMAGENES


    #CREAR GRUPOS
    TODOS = pg.sprite.Group()
    PLAYERS = pg.sprite.Group()
    BALAS = pg.sprite.Group()

    #CREAR OBJETOS
    nave = Nave()
    PLAYERS.add(nave)
    TODOS.add(nave)

    mira = Mira()
    TODOS.add(mira)




    #CICLO PRINCIPAL
    stop = False
    while stop == False:
        #RELOJ
        reloj.tick(FPS)

        #EVENTOS
        for event in pg.event.get():
            if event.type == pg.QUIT:
                stop = True
            if event.type == pg.MOUSEBUTTONDOWN:
                nave.disparar()

        #ACTUALIZAR
        TODOS.update()

        #RENDERIZAR
        ventana.fill(BLACK)
        TODOS.draw(ventana)

        #FLIP
        pg.display.flip()

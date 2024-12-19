import pygame as pg
from random import randint

placeholder = True
placeholderImg = pg.image.load("assets\sprites\placeholder.png")
terrainPlaceHolderImg = pg.image.load("assets\sprites/terrainPlaceholderImg.png")

class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = placeholderImg
        self.rect = self.image.get_rect()

        self.game = placeholder

        self.speed = 3

    def update(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_d] or keys[pg.K_RIGHT]:
            self.rect.x += 2 * self.speed
        
        if keys[pg.K_a] or keys[pg.K_LEFT]:
            self.rect.x -= 2 * self.speed

class terrain(pg.sprite.Sprite):
    def __init__(self,game):        
        pg.sprite.Sprite.__init__(self)        
        terrainSize = randint(20,100)
        self.image = pg.transform.scale(terrainPlaceHolderImg,(terrainSize,terrainSize))

        self.rect = self.image.get_rect()
        self.rect.y = randint(0,game.screenHeight)
        self.rect.x = randint(0,game.screenWidth)

    def update(self):
        pass
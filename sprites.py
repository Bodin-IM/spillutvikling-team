import pygame as pg

placeholder = True
placeholderImg = pg.image.load("assets\sprites\placeholder.png")

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


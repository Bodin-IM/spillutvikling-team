import pygame as pg

placeholder = True
placeholderPlayer = pg.image.load("assets\sprites\placeholder.png")
placeholderObstacle = pg.image.load("assets\sprites\pipe-placeholder.png")

class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = placeholderPlayer
        self.rect = self.image.get_rect()

        self.game = placeholder

        self.speed = 3

    def update(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_d] or keys[pg.K_RIGHT]:
            self.rect.x += self.speed
        
        if keys[pg.K_a] or keys[pg.K_LEFT]:
            self.rect.x -= self.speed

class Obstacle(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = placeholderObstacle
        self.rect = self.image.get_rect()

        self.game = placeholder 

        hit = pg.spritecollide(self, self.game.placeholder, True)
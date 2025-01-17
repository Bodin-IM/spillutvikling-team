import pygame as pg
from random import randint

placeholder = True
placeholderPlayer = pg.image.load("assets\sprites\placeholder.png")
placeholderObstacle = pg.image.load("assets\sprites\pipe-placeholder.png")
placeholderImg = pg.image.load("assets\sprites\placeholder.png")
terrainPlaceHolderImg = pg.image.load("assets\sprites/terrainPlaceholderImg.png")
wingedDeamonImg = pg.image.load("assets\sprites\wingedDeamon.png")
wingedDeamonAttackImg = pg.image.load("assets\sprites\wingedDeamonAttack.png")
fireProjectileImg = pg.image.load("assets\sprites/fireProjectile.png")

terrainImg = pg.image.load("assets\sprites/terrainClusterPart.png")


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

        if keys[pg.K_s] or keys[pg.K_DOWN]:
            self.rect.y += self.speed  

        if keys[pg.K_w] or keys[pg.K_UP]:
            self.rect.y -= self.speed  

class Obstacle(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = placeholderObstacle
        self.rect = self.image.get_rect()

        self.game = placeholder 

        hit = pg.spritecollide(self, self.game.placeholderGroup, True)
class terrain(pg.sprite.Sprite):
    def __init__(self,game, x, y):
        self.speed = 10      
        pg.sprite.Sprite.__init__(self)        
        terrainSize = randint(20,20)
        self.image = pg.transform.scale(terrainImg,(terrainSize,terrainSize))

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
    def update(self):
        pass


class wingedDeamon(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.attackingWingedDeamonFrames = [wingedDeamonImg, wingedDeamonAttackImg]
        self.wingedDeamonFrames = [wingedDeamonImg]
        self.attacking = False

    def update(self):
        self.animate

    def animate(self):
        now = pg.time.get_ticks()

        if self.attacking:
            if now - self.lastUpdate > 50:
                self.lastUpdate = now
                self.currentFrame = (self.currentFrame +1) % len(self.attackingWingedDeamonFrames)
                self.image = self.attackingWingedDeamonFrames[self.currentFrame]

        if self.attacking != True:
            if now - self.lastUpdate > 50:
                self.lastUpdate = now
                self.currentFrame = (self.currentFrame +1) % len(self.wingedDeamonFrames)
                self.image = self.wingedDeamonFrames[self.currentFrame]

class fireProjectile(pg.sprite.Sprite):
    def __init__(self, player, game):
        pg.sprite.Sprite.__init__(self)
    
        self.game = game

        self.lastUpdate = 0
        self.currentFrame = 0
        self.image = fireProjectileImg
        self.rect = self.image.get_rect()
        self.target = player

        self.rect.x = game.wingedDeamon.rect.x
        self.rect.y = game.wingedDeamon.rect.y

        self.speed.x = 3
        self.speed.y = 1

    def update(self):
        if self.rect.x > self.target.rect.x:
            self.rect.x -= self.speedX
        elif self.rect.x < self.target.rect.x:
            self.rect.x += self.speedX

        hit = pg.sprite.spritecollide(self, self.game.enemygroup, True)

    
class terrainCluster():
    def __init__(self,game, amount):
        self.blocks = []
        self.speed = 5
        origX = 500
        x = origX
        y = -1000
        lineAmount = 0
        newLine = 0
        for i in range(0,amount):
            block = terrain(game, x, y)
            
            x += block.image.get_width()
            

            if newLine <= 0:
                y += block.image.get_height()
                x = origX - block.image.get_width() * lineAmount //2
                lineAmount += 1
                newLine = lineAmount
                
            newLine -= 1

            self.blocks.append(block)
            game.allsprites.add(block)
            
    def update(self):
        for block in self.blocks:
            block.rect.y += self.speed


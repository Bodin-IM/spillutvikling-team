import pygame as pg
from sprites import *


class game():
    def __init__(self):
        pg.init()
        self.screenWidth = 1080
        self.screenHeight = 1080
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((self.screenWidth,self.screenHeight))
        self.new()


    def new(self):
        self.allsprites = pg.sprite.Group()
        self.enemyGroup = pg.sprite.Group()
        self.playerGroup = pg.sprite.Group()
        self.player = Player()
        self.allsprites.add(self.player)
        self.terrain = terrain(self)
        self.allsprites.add(self.terrain)
        self.run()

    def run(self):
        playing = True
        while playing:
            self.clock.tick(120)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    playing = False
            self.allsprites.update()
            self.allsprites.draw(self.screen)

            pg.display.update()

g = game()
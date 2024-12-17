import pygame as pg


class game():
    def __init__(self):
        pg.init()
        screenWidth = 1080
        screenHeight = 1080
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((screenWidth,screenHeight))
        self.new()


    def new(self):
        self.allsprites = pg.sprite.Group
        self.enemyGroup = pg.sprite.Group
        self.playerGroup = pg.sprite.Group

        self.run()
    def run(self):
        playing = True
        while playing:
            self.clock.tick(120)
            for event in pg.event.get():
                if event == pg.QUIT:
                    playing = False
            self.allsprites.update
            self.allsprites.draw








g = game()
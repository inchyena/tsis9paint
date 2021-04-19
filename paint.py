import os
import random

import pygame as pg


class App:

    def __init__(self):
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pg.init()
        self.w, self.h = 800, 600
        self.screen = pg.display.set_mode((self.w, self.h))
        self.screen.fill(pg.Color('white'))
        self.clock = pg.time.Clock()
        self.drawcolor = (0, 0, 0)

    def mainloop(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return
                elif event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 2:  #выбрать цвет кнопка посередине мышки
                        self.drawcolor = self.screen.get_at(pos)
                        # рандомный цвет
                        # self.drawcolor = [random.randrange(256) for _ in range(3)]
                elif event.type == pg.MOUSEMOTION:
                    pos, rel = event.pos, event.rel
                    if event.buttons[0]:  

                        pg.draw.line(self.screen, self.drawcolor, pos, (pos[0]-rel[0], pos[1]-rel[1]), 5)
                    elif event.buttons[2]:  
                        
                        pg.draw.circle(self.screen, (255, 255, 255), pos, 30)

            pg.display.flip()
            self.clock.tick(30)


if __name__ == '__main__':
    app = App()
    app.mainloop()
    pg.quit()
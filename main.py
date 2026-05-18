import sys
import pygame as pg
from utils import TimeManager,InputManager

class Engine:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((800, 600))
        pg.display.set_caption("CanvasPY Engine")   
        self.timer = TimeManager(fps_cap=60)
        self.inputs = InputManager()
        self.running = True

    def run(self):
        while self.running:
            dt = self.timer.tick()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
            self.inputs.update()
            if self.inputs.is_key_just_pressed(pg.K_SPACE):
                print(f"Spacebar tapped! Delta time is: {dt} seconds.")
                
            if self.inputs.is_key_held(pg.K_ESCAPE):
                self.running = False
            self.screen.fill((30,30,30))
            pg.display.flip()

        pg.quit()
        sys.exit()

if __name__ == "__main__":
    engine = Engine()
    engine.run()
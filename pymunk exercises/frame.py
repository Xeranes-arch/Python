import pymunk
import pymunk.pygame_util
import pygame


class Frame:

    def __init__(self):
        self.space = pymunk.Space()

    def run(self, grav=(0,100)):
        size = 1280, 720
        screen = pygame.display.set_mode(size)
        draw_options = pymunk.pygame_util.DrawOptions(screen)
        self.space.gravity = grav

        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            screen.fill((210, 210, 210))
            self.space.debug_draw(draw_options)
            pygame.display.update()
            self.space.step(0.001)
        

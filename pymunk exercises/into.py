import pymunk
import pymunk.pygame_util
import pygame


class frame:

    def __init__(self):
        self.space = pymunk.Space()

    def run(self):
        size = 1280, 720
        screen = pygame.display.set_mode(size)
        draw_options = pymunk.pygame_util.DrawOptions(screen)
        self.space.gravity = (0, 100)

        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            screen.fill((0, 0, 0))
            self.space.debug_draw(draw_options)
            pygame.display.update()
            self.space.step(0.001)
        pygame.display.update()



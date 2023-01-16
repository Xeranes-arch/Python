import pymunk
import pymunk.pygame_util
import pygame

pygame.init()
size = 640, 240
screen = pygame.display.set_mode(size)
draw_options = pymunk.pygame_util.DrawOptions(screen)

space = pymunk.Space()
space.gravity = 10, -100

b0 = space.static_body
segment = pymunk.Segment(b0, (0, 0), (640, 0), 4)
segment.elasticity = 1

body = pymunk.Body(mass=1, moment=10)
body.position = 100, 200

circle = pymunk.Circle(body, radius=20)
circle.elasticity = 0.95

space.add(body, circle, segment)

GRAY = (128, 128, 128)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill(GRAY)
    space.debug_draw(draw_options)
    pygame.display.update()
    space.step(0.005)
pygame.quit()
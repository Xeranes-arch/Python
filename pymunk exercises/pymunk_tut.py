import pymunk
import pymunk.pygame_util
import pygame

pygame.init()

size = 1280, 720
screen = pygame.display.set_mode(size)
draw_options = pymunk.pygame_util.DrawOptions(screen)

space = pymunk.Space()
space.gravity = (0, 100)

b0 = space.static_body
segment = pymunk.Segment(b0, (0, 520), (1280, 720), 4)
segment.elasticity = 0.5
segment.friction = 0.5
body = pymunk.Body(mass=1, moment=10)
body.position = 100, 100
circle = pymunk.Circle(body, radius=20)
circle.elasticity = 1
circle.friction = 0.5
# ADD
space.add(body, circle, segment)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill((0, 0, 0))
    space.debug_draw(draw_options)
    pygame.display.update()
    space.step(0.001)
pygame.display.update()


pygame.quit()

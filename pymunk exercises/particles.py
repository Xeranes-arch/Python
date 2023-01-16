import pymunk
import pymunk.pygame_util
import pygame
import random

from frame import Frame

game = Frame()

b0 = game.space.static_body
pts = [(0, 0), (1280, 0), (1280, 720), (0, 720)]
for i in range(4):
    segment = pymunk.Segment(b0, pts[i], pts[(i+1) % 4], 4)
    segment.elasticity = 0.999
    segment.friction = 0.999
    game.space.add(segment)

for i in range(100):

    body = pymunk.Body(mass=1, moment=10)
    body.position = (random.randint(0, 1280), random.randint(0, 720))
    body.apply_impulse_at_local_point(
        (random.randint(-100, 100), random.randint(-100, 100)))
    ball = pymunk.Circle(body, radius=10)
    ball.elasticity = 0.999999
    ball.friction = 0.999999
    game.space.add(body, ball)


grav = (0,0)
game.run(grav)

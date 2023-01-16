import pymunk
import pymunk.pygame_util
import pygame

from frame import Frame

game = Frame()

b0 = game.space.static_body
segment = pymunk.Segment(b0, (0, 520), (1280, 720), 4)
segment.elasticity = 0.5
segment.friction = 0.5
body = pymunk.Body(mass=1, moment=10)
body.position = 100, 100
circle = pymunk.Circle(body, radius=20)
circle.elasticity = 1
circle.friction = 0.5
game.space.add(body, circle, segment)

game.run()
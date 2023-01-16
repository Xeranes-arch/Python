import pymunk
import pymunk.pygame_util
import pygame
import random

from frame import Frame

game = Frame()

body = pymunk.Body(mass=1, moment=10)
body.position = (600, 200)
ball = pymunk.Circle(body, radius=20)
ball.elasticity = 0.99
ball.friction = 0.5
game.space.add(body, ball)
b0 = game.space.static_body
joint = pymunk.constraints.PinJoint(b0, body, (360, 200), (0, 0))
game.space.add(joint)

for i in range(4):
    body = pymunk.Body(mass=1, moment=10)
    body.position = (200 + i * 40, 440)
    ball = pymunk.Circle(body, radius=20)
    ball.elasticity = 0.99
    ball.friction = 0.5
    game.space.add(body, ball)
    b0 = game.space.static_body
    joint = pymunk.constraints.PinJoint(b0, body, (200 + 40 * i, 200), (0, 0))
    game.space.add(joint)

grav = (0, 100)
game.run(grav)

import pymunk
import pymunk.pygame_util
import pygame
import random


def main():
    print("This is GOT. \nYou place the ball, set its launch direction and initial speed as well as reset by left clicking. \nGot it? Let's go. Press Enter to start:")
    # input()
    # init pygame with world ready to play
    world = World()
    world.run()


class World:

    def __init__(self):
        # define screen
        size = (1280, 720)
        pts = [(0, 0), (size[0], 0), (size[0], size[1]), (0, size[1])]
        self.screen = pygame.display.set_mode(size)
        # create space
        self.space = pymunk.Space()
        self.space.gravity = (0, 981)
        # make world boundaries
        for i in range(4):
            segment = pymunk.Segment(
                self.space.static_body, pts[i], pts[(i+1) % 4], 4)
            segment.elasticity = 0.999
            segment.friction = 0.999
            self.space.add(segment)
        # make random  box target
        gsz = 60/2
        t_x = random.randint(100, 1180)
        t_y = random.randint(100, 620)
        self.pos_g = (t_x, t_y)
        t = pymunk.Body(mass=1, moment=10)
        print(self.pos_g)
        t.position = (self.pos_g)
        t1 = pymunk.Segment(self.space.static_body,
                            (t_x - gsz, t_y - gsz), (t_x - gsz, t_y + gsz), 2)
        t1.elasticity = 0.99999
        t1.friction = 0.999
        t2 = pymunk.Segment(self.space.static_body,
                            (t_x - gsz, t_y + gsz), (t_x + gsz, t_y + gsz), 2)
        t2.elasticity = 0.99999
        t2.friction = 0.999
        t3 = pymunk.Segment(self.space.static_body,
                            (t_x + gsz, t_y - gsz), (t_x + gsz, t_y + gsz), 2)
        t3.elasticity = 0.99999
        t3.friction = 0.999
        t3.angle = 0.5
        self.space.add(t, t1, t2, t3)
        # ball
        self.body = None
        self.ball = None

    def run(self):
        """Well. It runs the game."""
        draw_options = pymunk.pygame_util.DrawOptions(self.screen)
        # loop parameters
        n = 0
        update = False
        winable = False
        run = True
        while run:
            self.screen.fill((210, 210, 210))
            self.space.debug_draw(draw_options)
            pygame.display.update()
            for event in pygame.event.get():
                # quit
                if event.type == pygame.QUIT:
                    run = False
                # mouseclick; first, second, third, fourth
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if n == 0:
                        self.place_ball(pos)
                        winable = True
                        n += 1
                    elif n == 1:
                        self.set_dirandvel(pos)
                        n += 1
                    elif n == 2:
                        update = True
                        n += 1
                    elif n == 3:
                        self.reset()
                        update = False
                        n = 0
            # only run once user launches
            if update:
                self.space.step(0.001)
                # check win
                if (self.pos_g[0] - 50) < (self.body.position)[0] < (self.pos_g[0] + 50) and (self.pos_g[1] - 50) < self.body.position[1] < (self.pos_g[1] + 50) and winable:
                    print("You win! \nGo again if you like.")
                    winable = False

    def place_ball(self, pos):
        """places ball at given click position"""
        self.body = pymunk.Body(mass=1, moment=10)
        self.body.position = (pos)
        self.ball = pymunk.Circle(self.body, radius=20)
        self.ball.elasticity = 0.2
        self.ball.friction = 0.5
        self.space.add(self.body, self.ball)

    def set_dirandvel(self, pos):
        """should draw arrow to click and wait """

    def reset(self):
        """removes previous ball"""
        self.space.remove(self.body)
        self.space.remove(self.ball)

    def win(self):
        """should check if the player has scored, say so, end the game (and prompt play again)"""


if __name__ == "__main__":
    main()

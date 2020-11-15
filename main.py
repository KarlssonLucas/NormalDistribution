import pygame  # importing modules
import pymunk
import sys
from time import sleep


def create_falling_balls(space, pos):
    body = pymunk.Body(1, 100, body_type=pymunk.Body.DYNAMIC)
    body.position = pos
    shape = pymunk.Circle(body, 5)
    space.add(body, shape)
    return shape


def draw_fb(fbs):
    for fb in fbs:
        pos_x = int(fb.body.position.x)
        pos_y = int(fb.body.position.y)
        pygame.draw.circle(screen, (0, 0, 0), (pos_x, pos_y), 5)


def static_ball(space, pos):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = pos
    shape = pymunk.Circle(body, 5)
    space.add(body, shape)
    return shape


def draw_static_ball(balls):
    for ball in balls:
        pos_x = int(ball.body.position.x)
        pos_y = int(ball.body.position.y)
        pygame.draw.circle(screen, (217, 98, 119), (pos_x, pos_y), 5)


def create_board(space):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = (400, 800)
    w, h = 800, 10
    vs = [(-w / 2, -h / 2), (w / 2, -h / 2), (w / 2, h / 2), (-w / 2, h)]
    shape = pymunk.Poly(body, vs)
    space.add(body, shape)
    return shape


def create_pillar(space, pos):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = pos
    w, h = 1, 400
    vs = [(-w / 2, -h / 2), (w / 2, -h / 2), (w / 2, h / 2), (-w / 2, h)]
    shape = pymunk.Poly(body, vs)
    space.add(body, shape)
    return shape


def create_sides():
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = (25, 400)
    w, h = 1, 800
    vs = [(-w / 2, -h / 2), (w / 2, -h / 2), (w / 2, h / 2), (-w / 2, h)]
    shape = pymunk.Poly(body, vs)
    space.add(body, shape)

    body1 = pymunk.Body(body_type=pymunk.Body.STATIC)
    body1.position = (775, 400)
    shape = pymunk.Poly(body1, vs)
    space.add(body1, shape)


def create_align():
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = (300, 25)
    w, h = 1, 50
    vs = [(-w / 2, -h / 2), (w / 2, -h / 2), (w / 2, h / 2), (-w / 2, h)]
    shape = pymunk.Poly(body, vs)
    shape.color = (255, 0, 0, 255)
    space.add(body, shape)

    body1 = pymunk.Body(body_type=pymunk.Body.STATIC)
    body1.position = (500, 25)
    shape = pymunk.Poly(body1, vs)
    space.add(body1, shape)


def start_balls():
    pos = 1
    for i in range(0, 1000):
        pos *= -1
        fballs.append(create_falling_balls(space, (400 + 5*pos, 20-i)))
        pos += 1


def start_pillars():
    for i in range(75, 725, 50):
        create_pillar(space, (i, 800))


pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
space = pymunk.Space()
space.gravity = (0, 250)
fballs = []
create_sides()
create_align()

# EXTREMELY UGLY BUT TO TIRED TO COME UP WITH A SMARTER WAY #
balls = []
for i in range(0, 26):
    balls.append(static_ball(space, (25 + 30 * i, 300)))

for i in range(0, 25):
    balls.append(static_ball(space, (40 + 30 * i, 325)))

for i in range(0, 26):
    balls.append(static_ball(space, (25 + 30 * i, 350)))

for i in range(0, 25):
    balls.append(static_ball(space, (40 + 30 * i, 375)))

for i in range(0, 26):
    balls.append(static_ball(space, (25 + 30 * i, 400)))

for i in range(0, 25):
    balls.append(static_ball(space, (40 + 30 * i, 425)))

for i in range(0, 26):
    balls.append(static_ball(space, (25 + 30 * i, 450)))

for i in range(0, 25):
    balls.append(static_ball(space, (40 + 30 * i, 475)))

for i in range(0, 26):
    balls.append(static_ball(space, (25 + 30 * i, 500)))

for i in range(0, 25):
    balls.append(static_ball(space, (40 + 30 * i, 525)))

for i in range(0, 26):
    balls.append(static_ball(space, (25 + 30 * i, 550)))

for i in range(0, 25):
    balls.append(static_ball(space, (40 + 30 * i, 575)))


board = [create_board(space)]
start_balls()
start_pillars()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((217, 217, 217))
    draw_static_ball(balls)
    draw_fb(fballs)
    create_align()
    space.step(1 / 50)
    pygame.display.update()
    clock.tick(120)

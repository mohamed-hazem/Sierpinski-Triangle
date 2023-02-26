from random import randint, choice
import sys

import pygame as pg
pg.init()
# --------------------------- #
# Settings
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
R = (255, 0, 0)
G = (0, 255, 0)
B = (0, 0, 255)

COLORS = True

WIDTH, HEIGHT = (700,)*2
PIXEL_SIZE = 1

# Points with colors
POINTS = {
    (350, 100): R,
    (100, 600): G,
    (600, 600): B,
}
CORDS = [c for c in POINTS]

if not (COLORS):
    POINTS = {c: BLACK for c in POINTS}
# --------------------------- #
points = int(input("points: ").strip())
# --------------------------- #

# TEST FUNCTION
def random_point_on_line(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    m = (y2 - y1) / (x2 - x1)

    x = randint(x1, x2) if (x1 <= x2) else randint(x2, x1)
    y = m*x + m*(-x1)+y1

    return x, y
# --------------------------- #

# Window set
WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Sierpinski Triangle")
# --------------------------- #

# -- Main Functions -- #
def mid_point_on_line(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    
    return x, y

def add_point(point, color, win=WIN):
    x, y = point
    pg.draw.rect(win, color, (x*PIXEL_SIZE, y*PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))

# --------------------------- #
# initial grid
WIN.fill(WHITE)

add_point(CORDS[0], BLACK)
add_point(CORDS[1], BLACK)
add_point(CORDS[2], BLACK)

# initial points
main_point = choice(CORDS)
pre_point = choice(CORDS)

# -- Run Loop -- #
for i in range(points):
    try:
        color = POINTS[main_point]
        point = mid_point_on_line(main_point, pre_point)
        add_point(point, color)
    
        pre_point = point
    except ZeroDivisionError:
        pass
    
    main_point = choice(CORDS)

    pg.display.update()
    sys.stdout.write(f"\r[{i+1}] points")

    # Quit
    for event in pg.event.get():
        if (event.type == pg.QUIT):
            exit()
    
input("\nPress enter to exit ...")
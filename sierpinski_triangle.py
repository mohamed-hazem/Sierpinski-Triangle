from random import randint, choice
import sys

import pygame as pg
pg.init()
# --------------------------- #
# Settings
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

WIDTH, HEIGHT = (700,)*2
ROWS, COLS = (700,)*2

PIXEL_SIZE = WIDTH // COLS

P = [(350, 100), (100, 600), (600, 600)]
# --------------------------- #
points = int(input("points: ").strip())
# --------------------------- #

# TEST FUNCTION
def random_point_on_line(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    m = (y2 - y1) / (x2 - x1)

    x = randint(x1, x2) if (x1 <= x2) else randint(x2, x1)

    return x, int(x*m + m*(-x1)+y1)
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

add_point(P[0], BLACK)
add_point(P[1], BLACK)
add_point(P[2], BLACK)

# initial points
main_point = choice(P)
pre_point = choice(P)

# -- Run Loop -- #
for i in range(points):
    try:
        point = mid_point_on_line(main_point, pre_point)
        add_point(point, BLACK)
    
        pre_point = point
    except ZeroDivisionError:
        pass
    
    main_point = choice(P)

    pg.display.update()
    sys.stdout.write(f"\r[{i+1}] points")

    # Quit
    for event in pg.event.get():
        if (event.type == pg.QUIT):
            break
    
input("\nPress enter to exit ...")
from svg.path import Path, Line, Arc, CubicBezier, QuadraticBezier, Close, parse_path
import numpy
import pygame as pg
from svgpathtools import svg2paths
from collections import defaultdict
import cmath
from math import sin
import sys

def qudr(*args):
    arguments = args[::-1]
    def helper(x):
        ans = 0

        for i in range(len(arguments)):
            ans += (arguments[i]*(x**i))
        return ans
    return helper

func = qudr(1, 1, -1)

if (len(sys.argv) != 2):
    raise Exception("Not valid args, should be passed only one parrametr with path to SVG file")

paths, _= svg2paths(str(sys.argv[1]))

my_path = Path()

for i in paths:
    my_path.append(i)

prec_of_inter = 1000
screen_width = 700 
screen_height = 700
points = []

for i in numpy.arange (0, 1, 1 / prec_of_inter):
    t = (1 - i) * 2 - 1
    points.append((my_path.point(i).real / 184 - 0.5) + (my_path.point(i).imag / 184j + 0.5j))

prec = 125
arrows = defaultdict( lambda : 0)

sumz = sum(points)
start_x, start_y = sumz.real / prec_of_inter, (sumz.imag / prec_of_inter)

for i in range(1, prec // 2 + 1):
    for j in range(2):
        for t in numpy.arange(0, 1, 1 / prec_of_inter):
            arrows[i] += points[int(t * prec_of_inter)] * cmath.exp( -i * 2j * cmath.pi * -t)
        arrows[i] = arrows[i] / prec_of_inter
        i = -i

pg.init()
screen = pg.display.set_mode([screen_width, screen_height])
running = True
t = 0
figure = []
figure_size = prec_of_inter * 0.9
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.fill ((255, 255, 255))
    x, y = screen.get_size ()

    pg.draw.line (screen, (0, 0, 0), (x // 2, 0), (x // 2, y))
    pg.draw.line (screen, (0, 0, 0), (0, y // 2), (x, y // 2))

    start_from_x = start_x
    start_from_y = start_y
    pg.draw.line (screen, (0, 0, 0), (screen_width // 2, screen_height // 2), (start_x * (screen_width / 2) + (screen_width / 2) , start_y * ( - screen_height / 2 ) + (screen_height / 2)))
    for i in range(1, prec // 2 + 1):

        for j in range (2):
            i = -i
            end_point = cmath.exp (i * cmath.pi * 2j * t) * arrows[i] + (start_from_x + start_from_y *1j)

            end_x = end_point.real
            end_y = end_point.imag

            pg.draw.line(screen, (0, 0, 0), (start_from_x * (screen_width / 2) + (screen_width / 2), start_from_y  * (- screen_height / 2) + (screen_height / 2)),
                         (end_x * (screen_width / 2) + (screen_width / 2), end_y * (- screen_height / 2) + (screen_height / 2)))
            start_from_x = end_x
            start_from_y = end_y

    figure.append((start_from_x * (screen_width / 2) + (screen_width / 2), start_from_y  * (- screen_height / 2) + (screen_height / 2)))
    if len(figure) > figure_size:
        figure.pop(0)

    for i in figure:
        pg.draw.line(screen, (255, 64, 255), i, i)


    pg.display.flip ()
    t += 1 / prec_of_inter
    if t > 1:
        t = 0
pg.quit()
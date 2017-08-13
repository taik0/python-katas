#!/usr/bin/env python

from life import Life
from grid import Grid, LIVE
import time
import sys


# R-pentomino
r_seed = Grid(50,80)
r_coords = [
    (25,37), (25,38),
    (26,36), (26,37),
    (27,37)
]

for cell in r_coords:
    r_seed.set(cell[0], cell[1], LIVE)

# Pulsar
pulsar_seed = Grid(30,50)

pulsar_coords = [
    (1,5),(1,11),
    (2,5),(2,11),
    (3,5),(3,6),(3,10),(3,11),
    (5,1),(5,2),(5,3),(5,6),(5,7),(5,9),(5,10),(5,13),(5,14),(5,15),
    (6,3),(6,5),(6,7),(6,9),(6,11),(6,13),
    (7,5),(7,6),(7,10),(7,11),
    (9,5),(9,6),(9,10),(9,11),
    (10,3),(10,5),(10,7),(10,9),(10,11),(10,13),
    (11,1),(11,2),(11,3),(11,6),(11,7),(11,9),(11,10),(11,13),(11,14),(11,15),
    (13,5),(13,6),(13,10),(13,11),
    (14,5),(14,11),
    (15,5),(15,11)
    ]

for cell in pulsar_coords:
    pulsar_seed.set(cell[0], cell[1], LIVE)


game = Life(pulsar_seed)

counter = 0
while True:
    print game
    print "Counter: ", counter
    time.sleep(.1)
    game.tick()
    counter += 1

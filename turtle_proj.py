'''
Sai Anirvinya Kolli
9/15/2025
My turtle project
'''

import turtle
import random

class Walker:
    def __init__(self, pos, tu):
        self.pos = pos
        self.tu = tu 
        self.tu.goto(self.pos)

walkers = []
pos = []

for i in range(0, 50):
    tu = turtle.Turtle()
    tu.speed(0)
    position = [random.randint(-400, 400), random.randint(-400, 400)]
    w = Walker(position, tu)
    walkers.append(w)

for p in walkers:
    c = [random.randint(0,100), random.randint(0,100), random.randint(0,100)]
    for w in walkers:
        w.tu.color((c[0], c[1], c[2]))
        w.tu.goto(p.pos)
        w.tu.goto(w.pos)

turtle.done()
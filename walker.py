import turtle
import random

class Walker:
    def __init__(self, pos):
        self.pos = pos
        self.turt = turtle.Turtle()
        self.turt.penup()
        self.turt.speed(0)
        self.turt.goto(self.pos)
        self.turt.pendown()
        self.color = (random.uniform(0.5, 1), random.uniform(0.5, 1), random.uniform(0.5, 1))
    def move(self, target):
        self.turt.color(self.color)
        self.turt.goto(target)
        self.turt.goto(self.pos)

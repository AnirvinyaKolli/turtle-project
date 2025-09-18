import turtle
import random

class Walker:

    # Constructor
    def __init__(self, pos):

        # Setup 
        self.pos = pos
        self.turt = turtle.Turtle()
        self.turt.color("white")
        self.turt.penup()
        self.turt.speed(0)
        self.turt.goto(self.pos)
        self.turt.pendown()

        # Color randomization
        self.color = (random.uniform(0.5, 1), random.uniform(0.5, 1), random.uniform(0.5, 1))
    
    # Turtle movment method
    def move(self, target):
        self.turt.color(self.color)
        self.turt.goto(target)
        self.turt.goto(self.pos)

import colorsys
import turtle

class Walker:

    # Constructor
    def __init__(self, pos):
        self.pos = pos
        self.turt = turtle.Turtle()
        self.turt.color("white")
        self.turt.penup()
        self.turt.speed(0)
        self.turt.goto(self.pos)
        self.turt.pendown()
        self.color = (1, 0, 0)  

    # Chooses color based on previous color
    def set_color(self, prev_rgb, step=0.05):
        if prev_rgb is None:
            self.color = (1, 0, 0) 
            return
        h, s, v = colorsys.rgb_to_hsv(*prev_rgb)
        h = (h + step) % 1.0
        self.color = colorsys.hsv_to_rgb(h, s, v)

    # Turtle movement method
    def move(self, target):
        self.turt.goto(target)
        self.turt.goto(self.pos)
    
    def connect(self, targets):
        # Web connection drawing
        self.turt.color(self.color)
        for target in targets:
            self.move(target.pos)
        self.turt.color("white")

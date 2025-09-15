'''
Sai Anirvinya Kolli
9/15/2025
My turtle project
'''
from walker import Walker
from web import Web
import turtle
import random

background = turtle.Screen()
background.bgcolor("black")
background.title("Turtle Project")
background.screensize(400, 400)

web = Web("polygon", 100)
web.connect()

turtle.done()
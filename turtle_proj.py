'''
Sai Anirvinya Kolli
9/15/2025
My turtle project
'''
from walker import Walker
from web import Web
import turtle
import time

background = turtle.Screen()
background.bgcolor("black")
background.title("Turtle Project")
background.screensize(400, 400)

web = Web(web_type="random", num_walkers=20)
web.connect()
time.sleep(3)
background.clear()
background.bgcolor("black")

spiral_web = Web(web_type="spiral", num_walkers=20) 
spiral_web.connect()
time.sleep(3)
background.clear()
background.bgcolor("black")

polygon_web = Web(web_type="polygon", num_walkers=9)
polygon_web.connect()

turtle.done()
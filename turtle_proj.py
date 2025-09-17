'''
Sai Anirvinya Kolli
9/15/2025
My turtle project
'''
from walker import Walker
from webs import Web, SpiralWeb, PolygonWeb
import turtle

background = turtle.Screen()
background.bgcolor("black")
background.title("Turtle Project")
background.screensize(400, 400)

web = Web(num_walkers=10, bounds=400)
web.connect()
background.textinput("Pause", "Press Enter to continue...")
background.clear()
background.bgcolor("black")

spiral_web = SpiralWeb(num_walkers=10, bounds=400)
spiral_web.connect()
background.textinput("Pause", "Press Enter to continue...")
background.clear()
background.bgcolor("black")

polygon_web = PolygonWeb(num_walkers=9, bounds=400)
polygon_web.connect()

turtle.done()
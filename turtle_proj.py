'''
Sai Anirvinya Kolli
9/15/2025
My turtle project
'''
from walker import Walker
from webs import *
import random
import turtle
import time 

# Defines the types of webs 
web_types = ['spiral', 'random', 'polygon', 'wave' , 'constellation']

# Sets up screen 
background = turtle.Screen()
background.bgcolor("black")
background.title("Turtle Project")
background.screensize(400, 400)

# Defines quit function
quit = False
def end_main_loop():
    global quit
    quit = True

background.listen()
background.onkey(end_main_loop, "q")

# Main loop
while not quit:

    # Defining random values
    choice = random.choice(web_types) 
    rand_num_walkers = random.randint(6, 15)
    web = None
    match choice:
        case 'spiral':
            web = SpiralWeb(num_walkers=rand_num_walkers)
        case 'random':
            web = Web(num_walkers=rand_num_walkers)
        case 'polygon':
            web = PolygonWeb(num_walkers=rand_num_walkers)
        case 'wave':
            web = WaveWeb(num_walkers=rand_num_walkers)
        case 'constellation':
            web = ConstellationWeb(num_walkers=rand_num_walkers)
        case _:
            web = Web(num_walkers=rand_num_walkers)

    # Connections
    web.defineColors()
    web.connect()

    # Pause and screen reset
    time.sleep(1)
    background.clear()
    background.bgcolor("black")

    
background.bye()

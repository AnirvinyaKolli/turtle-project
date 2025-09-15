from walker import Walker
import turtle
import random
import math
class Web:
    def __init__(self, web_type="random",num_walkers=5, walkers=None):
        if walkers is None:
            match web_type:
                case "random":
                    self.walkers = self.random_web(num_walkers=num_walkers)
                case "polygon":
                    self.walkers = self.polygon_web(num_walkers=num_walkers)
                case _:
                    self.walkers = self.random_web(num_walkers=num_walkers)
        else:
            self.walkers = walkers

    def random_web(self,num_walkers=5,bounds=300):
        ws = [] 
        for i in range(0, num_walkers):
            position = [random.randint(-bounds, bounds), random.randint(-bounds, bounds)]
            w = Walker(position)
            ws.append(w)
        return ws
    
    def polygon_web(self,num_walkers=5,radius=300):
        angleIncrement = 360 / num_walkers 
        ws = [] 
        angle = 0
        for i in range(0, num_walkers):
            x = radius * math.cos(math.radians(angle))
            y = radius * math.sin(math.radians(angle))
            position = [x, y]
            w = Walker(position)
            ws.append(w)
            angle += angleIncrement
        return ws

    def connect(self):
        for i in range(len(self.walkers)):
            for j in range(i + 1, len(self.walkers)):
                self.walkers[i].move(self.walkers[j].pos)
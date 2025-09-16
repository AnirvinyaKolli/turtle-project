from walker import Walker
import random
import math
class Web:
    def __init__(self,num_walkers=5, bounds = 400, walkers=None):
        if walkers is None:
            self.walkers = self.generate_web(num_walkers=num_walkers, bounds=bounds)
        else:
            self.walkers = walkers

    def generate_web(self,num_walkers=5,bounds=300):
        ws = [] 
        for i in range(0, num_walkers):
            position = [random.randint(-bounds, bounds), random.randint(-bounds, bounds)]
            w = Walker(position)
            ws.append(w)
        return ws
            
    def connect(self):
        for i in range(len(self.walkers)):
            for j in range(i + 1, len(self.walkers)):
                self.walkers[i].move(self.walkers[j].pos)

class SpiralWeb(Web):
    def __init__(self,num_walkers=5,bounds=300):
        super().__init__(num_walkers=num_walkers, bounds=bounds)

    def generate_web(self,num_walkers=5,bounds=300):
       angleIncrement = 360 / num_walkers 
       ws = [] 
       angle = 0
       current_radius = 0
       for i in range(0, num_walkers):
            x = current_radius * math.cos(math.radians(angle))
            print(f"Cos = {math.cos(math.radians(angle))}")
            y = current_radius * math.sin(math.radians(angle))
            print(f"Sin = {math.sin(math.radians(angle))}")
            position = [x, y]
            w = Walker(position)
            ws.append(w)
            print (f"Current Radius pre inc = {current_radius}, {i}")
            angle += angleIncrement
            current_radius += bounds / num_walkers
            print (f"Current Radius = {current_radius}")
       return ws

class PolygonWeb(Web):
    def __init__(self,num_walkers=5,bounds=300):
        super().__init__(num_walkers=num_walkers, bounds=bounds)

    def generate_web(self,num_walkers=5,bounds=300):
        angleIncrement = 360 / num_walkers 
        ws = [] 
        angle = 0
        for i in range(0, num_walkers):
            x = bounds * math.cos(math.radians(angle))
            y = bounds * math.sin(math.radians(angle))
            position = [x, y]
            w = Walker(position)
            ws.append(w)
            angle += angleIncrement
        return ws
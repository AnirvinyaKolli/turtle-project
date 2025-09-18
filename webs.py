from walker import Walker
import random
import math

# Web parent class 
class Web:

    def __init__(self,num_walkers=5, bounds = 400, walkers=None):

        # Generates walkers if not given
        if walkers is None:
            self.walkers = self.generate_web(num_walkers=num_walkers, bounds=bounds)
        else:
            self.walkers = walkers

    def generate_web(self,num_walkers=5,bounds=300):

        # Base web generator (random)
        ws = [] 
        for i in range(0, num_walkers):
            position = [random.randint(-bounds, bounds), random.randint(-bounds, bounds)]
            w = Walker(position)
            ws.append(w)
        return ws
            
    def connect(self):

        # Web connection drawing
        for i in range(len(self.walkers)):
            for j in range(i + 1, len(self.walkers)):
                self.walkers[i].move(self.walkers[j].pos)

# Spiral extension of web
class SpiralWeb(Web):

    # Constructor
    def __init__(self,num_walkers=5,bounds=300):
        super().__init__(num_walkers=num_walkers, bounds=bounds)

    # Spiral web generator override 
    def generate_web(self,num_walkers=5,bounds=300):
       angleIncrement = 360 / num_walkers 
       ws = [] 
       angle = 0
       current_radius = 0
       for i in range(0, num_walkers):
            x = current_radius * math.cos(math.radians(angle))
            y = current_radius * math.sin(math.radians(angle))
            position = [x, y]
            w = Walker(position)
            ws.append(w)
            angle += angleIncrement
            current_radius += bounds / num_walkers
       return ws

# Spiral extension of web
class PolygonWeb(Web):

    # Constructor
    def __init__(self,num_walkers=5,bounds=300):
        super().__init__(num_walkers=num_walkers, bounds=bounds)
    
    # Polygon web generator override
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

# Wave extension of web (LLM added)
class WaveWeb(Web):

    # Constructor
    def __init__(self, num_walkers=5, bounds=300, amplitude=100, frequency=1):
        self.amplitude = amplitude
        self.frequency = frequency
        super().__init__(num_walkers=num_walkers, bounds=bounds)

    # Wave web generator override
    def generate_web(self, num_walkers=5, bounds=300):
        ws = []
        x_spacing = bounds * 2 / (num_walkers - 1)  # Spread across -bounds to +bounds
        for i in range(num_walkers):
            x = -bounds + i * x_spacing
            y = self.amplitude * math.sin(self.frequency * math.radians(x))
            position = [x, y]
            w = Walker(position)
            ws.append(w)
        return ws

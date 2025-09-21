from walker import Walker
import random
import math

# Web parent class 
class Web:

    def __init__(self,num_walkers=5, bounds = 300, walkers=None):

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
            ws.append(Walker(position))
        return ws
            
    def connect(self):
        # Web connection drawing
        targets = self.walkers.copy()
        for walker in self.walkers:
            walker.connect(targets)
            targets.remove(walker)
    
    def defineColors(self):
        prev_color = None
        for walker in self.walkers:
            walker.set_color(prev_color)
            prev_color = walker.color

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
            ws.append(Walker(position))
            angle += angleIncrement
        return ws

# Wave extension of web (LLM added)
class WaveWeb(Web):

    # Constructor
    def __init__(self, num_walkers=5, bounds=300, amplitude=100, frequency=1):
        self.amplitude = amplitude
        self.frequency = frequency
        super().__init__(num_walkers=num_walkers, bounds=bounds)

    # Wave web generator
    def generate_web(self, num_walkers=5, bounds=300):
        ws = []
        x_spacing = bounds * 2 / (num_walkers - 1)  # Spread across -bounds to +bounds
        for i in range(num_walkers):
            x = -bounds + i * x_spacing
            # Use a full sine wave cycle across all walkers
            phase = (i / (num_walkers - 1)) * 2 * math.pi * self.frequency
            y = self.amplitude * math.sin(phase)
            position = [x, y]
            w = Walker(position)
            ws.append(w)
        return ws



# Constellation extension of web
class ConstellationWeb(Web):
    def __init__(self, num_walkers=5, bounds=300):
        super().__init__(num_walkers=num_walkers, bounds=bounds)

        # Sets threshold and branches
        self.threshold = self.find_threshold(num_walkers, bounds)
        self.walker_branches = []
        for walker in self.walkers:
            branches = self.find_branches(walker)
            self.walker_branches.append([walker, branches])

    # Defines all walker colors to yellow
    def defineColors(self):
        for walker in self.walkers:
            walker.color = "yellow"

    # Finds threshold distance for connections
    def find_threshold(self, num_walkers, bounds):
        bias = 3
        threshold = bounds / math.sqrt(math.pi * (num_walkers - 1))
        return threshold * bias

    # Finds branches for each walker
    def find_branches(self, walker):
        bw = []
        dists = {}
        distances = []
        for other in self.walkers:
            if other == walker:
                continue
            distance = math.sqrt((walker.pos[0]-other.pos[0])**2 + (walker.pos[1] - other.pos[1])**2)
            dists[distance] = other
            distances.append(distance)
        distances.sort()
        if distances[0] > self.threshold and distances is not None and distances[0]:
            bw.append(dists[distances[0]])
            return bw
        for distance in distances:
            if distance < self.threshold:
                bw.append(dists[distance])
            else:
                return bw
    
    # Connect method override
    def connect(self):
        for wb in self.walker_branches:
            wb[0].turt.color(wb[0].color)
            for branch in wb[1]:
                wb[0].move(branch.pos)
            wb[0].turt.color("white")
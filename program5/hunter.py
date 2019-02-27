# Hunter is derived both from the Mobile_Simulton/Pulsator classes; each updates
#   like a Pulsator, but it also moves (either in a straight line
#   or in pursuit of Prey), and displays as a Pulsator.


from prey import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2
import math 
import random

class Hunter(Pulsator, Mobile_Simulton):
    d = 200
    def __init__(self, x, y):
        Pulsator.__init__(self, x, y)
        Mobile_Simulton.__init__(self, x, y, self.get_dimension()[0], self.get_dimension()[1], 2*math.pi*random.random(), 5)
        
    def update(self, model):
        already_eaten = Pulsator.update(self, model)
        all_prey = model.find(lambda s: isinstance(s, Prey) and Hunter.d >= self.distance(s.get_location()))
        target = None
        target_distance = None
        if len(all_prey) != 0:
            for t in all_prey:
                if target == None:
                    target = t
                if target_distance == None:
                    target_distance = self.distance(t.get_location())
                if self.distance(t.get_location()) < target_distance:
                    target_distance = self.distance(t.get_location())
                    target = t
            self_x = self.get_location()[0]
            self_y = self.get_location()[1]
            target_x, target_y = target.get_location()
            self.set_angle(atan2(target_y-self_y, target_x - self_x))
        self.move()
        
        
        
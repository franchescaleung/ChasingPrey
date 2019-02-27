#Special class
#every time a ball touches the green hole, a new ball is added
#when a ball is added and before the ball leaves the parameter of the green hole, the green hole may detect the balls and add more
#acts like a Simulton
#radius = 10
from simulton import Simulton
from prey import Prey
from ball import Ball
import math
import random

class Special(Simulton):
    def __init__(self, x, y):
        Simulton.__init__(self, x, y, 10, 10)
    def display(self, the_canvas):
        the_canvas.create_oval(self._x-self.get_dimension()[0], self._y-self.get_dimension()[1],
                                self._x+self.get_dimension()[0], self._y+self.get_dimension()[1],
                                fill="#8ae0c5")
     
    def update(self, model):
        for sim in model.all_simultons.copy():
            if self.contains(sim.get_location()) and isinstance(sim, Ball):
                model.all_simultons.add(eval('Ball(' + str(self.get_location()[0]) + ',' + str(self.get_location()[1]) + ')'))
                    


    def contains(self, xy):
        d = self.distance(xy)
        dimensions = self.get_dimension()
        return self.distance(xy) <= dimensions[1]/2

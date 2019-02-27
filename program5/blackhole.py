# Black_Hole is derived from the Simulton: each updates by finding and removing
#   any Prey whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey


class Black_Hole(Simulton):
    radius = 10
    def __init__(self, x,y):
        #what about color
        Simulton.__init__(self,x,y,2*Black_Hole.radius,2*Black_Hole.radius)
        self._eaten = set()
    def update(self, model):
        for sim in model.all_simultons.copy():
            if self.contains(sim.get_location()) and isinstance(sim, Prey):
                self._eaten.add(sim)
                model.remove(sim)
        return self._eaten

    def display(self, canvas):
        canvas.create_oval(self._x-self.get_dimension()[0], self._y-self.get_dimension()[1],
                                self._x+self.get_dimension()[0], self._y+self.get_dimension()[1],
                                fill="#000000")
    def contains(self, xy):
        d = self.distance(xy)
        dimensions = self.get_dimension()
        return self.distance(xy) <= dimensions[1]/2

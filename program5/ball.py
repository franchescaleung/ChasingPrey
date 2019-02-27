# A Ball is Prey; it updates by moving in a straight
#   line and displays as blue circle with a radius
#   of 5 (width/height 10).

from prey import Prey
import math
import random

class Ball(Prey): 
    radius = 5
    def __init__(self, x,y):
        #what about color
        Prey.__init__(self,x,y,2*Ball.radius,2*Ball.radius, 2*math.pi*random.random(), 5)
    def update(self, model):
        self.move()

    def display(self, canvas):
        canvas.create_oval(self._x-Ball.radius, self._y-Ball.radius,
                                self._x+Ball.radius, self._y+Ball.radius,
                                fill="black")

# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage


from PIL.ImageTk import PhotoImage
from prey import Prey
import random
import math

class Floater(Prey): 
    def __init__(self, x, y):
        self._image = PhotoImage(file='ufo.gif')
        Prey.__init__(self, x, y, self._image.width(), self._image.height(), 2*math.pi*random.random(), 5)

    def update(self,model):
        temp = random.randint(1,10)
        if temp <= 3:
            #change angle and speed
            a = random.choice('+-')
            b = random.choice('+-')
            changedby1 = int(str(a) + str(random.randint(0,5))) * .1
            changedby2 = int(str(b) + str(random.randint(0, 5))) * .1
            if ((self.get_speed() + changedby1) <= 7) or ((self.get_speed() + changedby1) >= 3):
                self.set_speed(self.get_speed() + changedby1)
            self.set_angle(self.get_angle() + changedby2)
        self.move()
        
    def display(self,the_canvas):
        the_canvas.create_image(*self.get_location(),image=self._image)
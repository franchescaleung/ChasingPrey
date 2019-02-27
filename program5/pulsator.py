# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions


from blackhole import Black_Hole


class Pulsator(Black_Hole): 
    constant = 30
    def __init__(self, x,y):
        #what about color
        Black_Hole.__init__(self,x,y)
        self._counter = 0
        self.count = 0
   
    
    def update(self, model):
        self._counter += 1
        already_eaten = Black_Hole.update(self,model)
        if already_eaten and len(already_eaten) > self.count:
            self.count += 1
            self.change_dimension(len(already_eaten), len(already_eaten))
            self._counter = 0
        elif self._counter == Pulsator.constant:
            self.change_dimension(-1, -1)
            if self.get_dimension() == (0,0):
                model.remove(self)
            self._counter = 0
        return already_eaten
            
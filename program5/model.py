import controller, sys
import model   # Pass a reference to this module to each update call in update_all

#Use the reference to this module to pass it to update methods

from ball      import Ball
from floater   import Floater
from blackhole import Black_Hole
from pulsator  import Pulsator
from hunter    import Hunter
from special   import Special

# Global variables: declare them global in functions that assign to them: e.g., ... = or +=

running     = False
cycle_count = 0
all_simultons = set()
object_clicked = None
#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global running,cycle_count,balls
    running     = False
    cycle_count = 0
    all_simultons.clear() 


#start running the simulation
def start ():
    global running
    running = True


#stop running the simulation (freezing it)
def stop ():
    global running
    running = False


#tep just one update in the simulation
def step ():
    global running, cycle_count
    if not running:
        cycle_count += 1
        for sim in all_simultons.copy():
            sim.update(model)
    else:
        for sim in all_simultons.copy():
            sim.update(model)
        stop()
    


#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global object_clicked
    object_clicked = kind
    print(object_clicked)


#add the kind of remembered object to the simulation (or remove all objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    global object_clicked
    if object_clicked == 'Remove':
        for sim in all_simultons:
            if sim.contains((x,y)):
                remove(sim)
                break
    else:
        add(eval(str(object_clicked) + '(' + str(x) + ',' + str(y) + ')'))
        

#add simulton s to the simulation
def add(s):
    global all_simultons
    all_simultons.add(s)
   

# remove simulton s from the simulation    
def remove(s):
    global all_simultons
    all_simultons.discard(s)
    
    
    

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    global all_simultons
    a = set()
    for sim in all_simultons:
        if p(sim):
            a.add(sim)
    return a


#call update for each simulton in the simulation (pass the model as an argument)
#this function should loop over one set containing all the simultons
#  and should not call type or isinstance: let each simulton do the
#  right thing for itself, without this function knowing what kinds of
#  simultons are in the simulation
def update_all():
    global cycle_count, running
    if running:
        cycle_count += 1
        set_sim = set(all_simultons)
        for sim in set_sim:
            sim.update(model)


#delete from the canvas every simulton being simulated; next call display on every
#  simulton being simulated to add it back to the canvas, possibly in a new location, to
#  animate it; also, update the progress label defined in the controller
#this function should loop over one set containing all the simultons
#  and should not call type or isinstance: let each simulton do the
#  right thing for itself, without this function knowing what kinds of
#  simultons are in the simulation
def display_all():
    for o in controller.the_canvas.find_all():
        controller.the_canvas.delete(o)
    
    for sim in all_simultons:
        sim.display(controller.the_canvas)
    
    controller.the_progress.config(text=str(str(cycle_count)+" cycles/" + str(len(all_simultons))+" simultons"))

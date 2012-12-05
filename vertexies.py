import pyglet
from pyglet.window import mouse
from squares import Square, Square2
from button import Button

window = pyglet.window.Window()

class Environment(object):
    def __init__(self):
        self.button_list = []
        self.button_batch = pyglet.graphics.Batch()
        self.obj_list = []
        self.batch = pyglet.graphics.Batch()
    def draw(self):
        self.batch.draw()
        self.button_batch.draw()
        
environment = Environment()

environment.button_list.append(Button(environment, window.width-50, 300))

def update(dt):
    for obj in environment.obj_list:
        obj.update(dt)
    for bt in environment.button_list:
        bt.update(dt)

@window.event
def on_draw():
    window.clear()
    environment.draw()

@window.event
def on_mouse_press(x, y, button, modifiers):
    '''check if in menu'''
    if x>window.width-100:
        for bt in environment.button_list:
            bt.active = True
    ''' Click to make a square'''
    if button == mouse.LEFT: #blue
        environment.obj_list.append(Square(environment,x,y))

    if button == mouse.RIGHT: #white
        environment.obj_list.append(Square2(environment,x,y))
        
@window.event
def on_mouse_drag(x, y, dx,dy,button, modifiers):
    ''' Drag to set the size of the body'''
    environment.obj_list[-1].resize(x,y)

@window.event
def on_mouse_release(x, y, button, modifiers):
    ''' When uncommented, demonstrates changinging a 
           specific body regardless of the body type'''
    for s in environment.obj_list:
        s.active = True
    #last = len(environment.obj_list)
    #if last > 1:    
    #    environment.obj_list[last-2].relocate(0,0)

dt = 1/30.
pyglet.clock.schedule_interval(update, dt) # Schedules updates for all objects every 30th of a second (Float)


pyglet.app.run()



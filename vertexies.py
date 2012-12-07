import pyglet
from pyglet.window import mouse, key
from bodies import Square, Circle

window = pyglet.window.Window()

class Environment(object):
    def __init__(self):
        self.active = True
        self.mode = 's'     # modes are s -> square, c -> circle
        self.obj_list = []
        self.batch = pyglet.graphics.Batch()
    def draw(self):
        self.batch.draw()
        
        
environment = Environment()


@window.event
def on_draw():
    window.clear()
    environment.draw()

@window.event
def on_mouse_press(x, y, button, modifiers):
    ''' Click to make a square'''
    if button == mouse.LEFT: #blue
        environment.obj_list.append(Square(environment,x,y))

    if button == mouse.RIGHT: #white
        environment.obj_list.append(Circle(environment,x,y))
        
@window.event
def on_mouse_drag(x, y, dx,dy,button, modifiers):
    ''' Drag to set the size of the body'''
    environment.obj_list[-1].set_size(x,y)

@window.event
def on_mouse_release(x, y, button, modifiers):
    for s in environment.obj_list:
        s.active = True

@window.event
def on_key_press(symbol, modifiers):
    if key.symbol_string(symbol) == 'SPACE':
        environment.active = False

def  update(dt):
    if environment.active:
        for obj in environment.obj_list:
            obj.update(dt)

dt = 1/30.
pyglet.clock.schedule_interval(update, dt) # Schedules updates for all objects every 30th of a second (Float)


pyglet.app.run()



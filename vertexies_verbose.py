import pyglet
from pyglet.window import mouse, key
from bodies import Square, Circle

window = pyglet.window.Window()

class Environment(object):
    def __init__(self):
        self.menu_batch = pyglet.graphics.Batch()
        width = window.width
        self.menu_batch.add(4, pyglet.gl.GL_QUADS, None, 
            ('v2i', (0,0,width,0,width,30,0,30)),
            ('c3B', (20,40,100)*4))
        self.menu_active = pyglet.text.Label('RUNNING',
                          font_name='Times New Roman',
                          font_size=15,
                          batch = self.menu_batch,
                          x=15, y=15,
                          anchor_x='left', anchor_y='center')
        self.menu_mode = pyglet.text.Label('CIRCLE',
                          font_name='Times New Roman',
                          font_size=15,
                          batch = self.menu_batch,
                          x=200, y=15,
                          anchor_x='left', anchor_y='center')
        self.instructions = pyglet.text.Label('\'space\' to pause/unpause\t\'C\' for circles\t\'S\' for squares',
                          font_name='Times New Roman',
                          font_size=12,
                          batch = self.menu_batch,
                          x=width - 15, y=15,
                          anchor_x='right', anchor_y='center')


        self.active = True
        self.mode = 'C'     # modes are s -> square, c -> circle
        self.obj_list = []
        self.batch = pyglet.graphics.Batch()

    def update(self):
        if self.active:
            self.menu_active.text = 'RUNNING'
        else:
            self.menu_active.text = 'PAUSED'
        if self.mode == 'C':
            self.menu_mode.text = 'CIRCLE'
        else:
            self.menu_mode.text = 'SQUARE'

    def draw(self):
        self.batch.draw()
        self.menu_batch.draw()
        
environment = Environment()


@window.event
def on_draw():
    window.clear()
    environment.draw()

@window.event
def on_mouse_press(x, y, button, modifiers):
    ''' Click to make a square'''
    if environment.mode == 'S': #square
        environment.obj_list.append(Square(environment,x,y))

    if environment.mode == 'C': #circle
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
        environment.active = not environment.active
    if key.symbol_string(symbol) == 'S':
        environment.mode = 'S'
    if key.symbol_string(symbol) == 'C':
        environment.mode = 'C'

def  update(dt):
    environment.update()
    if environment.active:
        for obj in environment.obj_list:
            obj.update(dt)

dt = 1/30.
pyglet.clock.schedule_interval(update, dt) # Schedules updates for all objects every 30th of a second (Float)


pyglet.app.run()



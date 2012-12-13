import pyglet
from pyglet.window import mouse, key
from bodies import Square, Circle, Rod

window = pyglet.window.Window(width=800,height=600)

class Environment(object):
    def __init__(self):
        self.menu_batch = pyglet.graphics.Batch()
        width = window.width
        self.menu_batch.add(4, pyglet.gl.GL_QUADS, None, 
            ('v2i', (0,0,width,0,width,30,0,30)),
            ('c3B', (20,40,100)*4))
        self.menu_active = pyglet.text.Label('START',
                          font_name='Times New Roman',
                          font_size=15,
                          batch = self.menu_batch,
                          x=15, y=15,
                          anchor_x='left', anchor_y='center')
        self.menu_mode = pyglet.text.Label('CIRCLE',
                          font_name='Times New Roman',
                          font_size=15,
                          batch = self.menu_batch,
                          x=150, y=15,
                          anchor_x='left', anchor_y='center')
        self.instructions = pyglet.text.Label('\'space\' to pause/unpause \t\t \'t\' to select \t\t \'c\' for circles \t \'s\' for squares \t \'r\' for rods',
                          font_name='Times New Roman',
                          font_size=12,
                          batch = self.menu_batch,
                          x=width - 15, y=15,
                          anchor_x='right', anchor_y='center')

        self.active = True
        self.mode = 'T'     # modes are s -> square, c -> circle, R -> rod, T -> select
        self.obj_list = []
        self.batch = pyglet.graphics.Batch()
        self.track_batch = pyglet.graphics.Batch()

    def update(self):
        if self.active:
            self.menu_active.text = 'RUNNING'
        else:
            self.menu_active.text = 'PAUSED'
        if self.mode == 'C':
            self.menu_mode.text = 'CIRCLE'
        elif self.mode == 'S':
            self.menu_mode.text = 'SQUARE'
        elif self.mode == 'R':
            self.menu_mode.text = 'ROD'
        else:
            self.menu_mode.text = 'select'

    def draw(self):
        self.batch.draw()
        self.menu_batch.draw()
        self.track_batch.draw()
        
environment = Environment()


@window.event
def on_draw():
    window.clear()
    environment.draw()

@window.event
def on_mouse_press(x, y, button, modifiers):
    ''' Click to make a shape'''
    mode = environment.mode
    if mode == 'S': #square
        environment.obj_list.append(Square(environment,x,y))
    if mode == 'C': #circle
        environment.obj_list.append(Circle(environment,x,y))
    if mode == 'R': #rod
        environment.obj_list.append(Rod(environment,x,y))
    if mode == 'T': #select
        for obj in environment.obj_list:
            if obj.is_inside(x,y):
                obj.add_anchor(x,y)
        
@window.event
def on_mouse_drag(x, y, dx,dy,button, modifiers):
    ''' Drag to set the size of the shape'''
    if environment.mode in ['S','C','R']:
        environment.obj_list[-1].set_size(x,y)


@window.event
def on_mouse_release(x, y, button, modifiers):
    '''activate the bodies once made'''
    for s in environment.obj_list:
        s.active = True

@window.event
def on_key_press(symbol, modifiers):
    ''' change the drawing mode or pause the system'''
    if key.symbol_string(symbol) == 'SPACE':
        environment.active = not environment.active
    else:
        environment.mode = key.symbol_string(symbol)

def update(dt):
    environment.update()
    if environment.active:
        for obj in environment.obj_list:
            obj.update(dt)

environment.obj_list.append(Circle(environment,200,500))
environment.obj_list[-1].set_size(205,505)
environment.obj_list[-1].joinToObject(fixPoint=(400,600),fixVelocity=(0,0))
environment.obj_list.append(Circle(environment,180,400))
environment.obj_list[-1].set_size(185,405)
environment.obj_list[-1].joinToObject(body=environment.obj_list[-2])

dt = 1/60.

pyglet.clock.schedule_interval(update, dt) # Schedules updates for all objects every 30th of a second (Float)


pyglet.app.run()



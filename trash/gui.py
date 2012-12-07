import pyglet

window = pyglet.window.Window()

class Environment(object):
    def __init__(self):
        self.obj_ls = []
        self.obj_batch = pyglet.graphics.Batch()
        
environment = Environment()

class Circle(object):
    def __init__(self, x=0, y=0, r=10):
        self.x = x
        self.y = y
        self.radius = r

mycircle = Circle()

class Line(object):
    def __init__(self, x1=0, y1=0, x2=10, y2=10):
        self.x1=x1
        self.x2=x2
        self.y1=y1
        self.y2=y2
 
line=Line()

def update(dt):
    for obj in environment.obj_ls:
        obj.update(dt)

@window.event
def on_mouse_motion(x, y, dx, dy):
#    print dx, dy
    pass

@window.event
def on_mouse_press(x, y, button, modifiers):
    line.x1 = x
    line.y1 = y

@window.event
def on_mouse_release(x, y, button, modifiers):
    pass

@window.event
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    line.x2 = x
    line.y2 = y
    print line.x1, line.y1, line.x2, line.y2
    pyglet.graphics.draw(2, pyglet.gl.GL_LINES, 
    ('v2f', (line.x1, line.y1, line.x2, line.y2)))


@window.event
def on_draw():
    window.clear()
    environment.obj_batch.draw()


dt = 1/30.
pyglet.clock.schedule_interval(update, dt) # Schedules updates for all objects every 30th of a second (Float)


#def update(dt):
    


if __name__ == "__main__":
    pyglet.app.run()

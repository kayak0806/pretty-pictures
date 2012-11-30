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
 

def update(dt):
    for obj in environment.obj_ls:
        obj.update(dt)

@window.event
def on_mouse_motion(x, y, dx, dy):
#    print dx, dy
    pass

@window.event
def on_mouse_press(x, y, button, modifiers):
    pass

@window.event
def on_mouse_release(x, y, button, modifiers):
    print mycircle.x, mycircle.y, mycircle.radius
    pyglet.graphics.draw(1, pyglet.gl.GL_POINTS, ('v2i', (mycircle.x, mycircle.y)))

@window.event
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    mycircle.x = x
    mycircle.y = y
    r = ((x-dx)**2 + (y-dy)**2)**.5
    mycircle.radius = r

@window.event
def on_draw():
    window.clear()
    environment.obj_batch.draw()


environment.obj_ls.append(mycircle)




if __name__ == "__main__":
    pyglet.app.run()

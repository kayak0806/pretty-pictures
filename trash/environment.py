
import pyglet

class Environment(object):
    def __init__(self):
        self.obj_ls = []
        self.obj_batch = pyglet.graphics.Batch()
        
    def draw(self):
        self.obj_batch.draw()
        
    def update(self,dt):
        for obj in self.obj_ls:
            obj.update(dt)



'''

Simple environment/body animation code.

Environments contain a batch of drawable objects (bodies). Environment.draw() draws everything in the environment.

bodies contain a tuple of points

Rachel Boy, Slater, Diana for room-arranger + collision-checking
'''
import pyglet

window = pyglet.window.Window()

class Environment(object):
    def __init__(self):
        self.obj_ls = []
        self.obj_batch = pyglet.graphics.Batch()
        
    def draw(self):
        self.obj_batch.draw()
        
environment = Environment()
        
class body(object):
    
    def __init__(self,environment, points = (0,0),color = None):
        if color == None:
            self.vertex_list = environment.obj_batch.add(len(points)/2,
                pyglet.gl.GL_POLYGON, None,('v2f',points)
            )
        else:
            self.vertex_list = environment.obj_batch.add(len(points)/2,
                pyglet.gl.GL_POLYGON, None,('v2f',points),('c3B',color)
            )
            
        self.points = points
        
        
    # Not relevant with the current setup: we always draw from the Environment's obj_batch, which draws objects (vector lists) as they were added. This would be relevant if we wanted to draw objects individually, without calling their vector_lists. 
    #def draw(self,arg=pyglet.gl.GL_POLYGON):
    #    self.vertex_list.draw(arg)
        
    def update(self,dt):
        points = ()
        for i in range(len(self.points)):
            #print self.vertex_list.vertices[i]
            #self.vertex_list.vertices[i] = self.vertex_list.vertices[i] + 10
            points += (self.points[i] + 10,)
            
        self.points = points
        self.refresh_vertices()
        
    def refresh_vertices(self):
        self.vertex_list.vertices = self.points

@window.event
def on_draw():
    window.clear()
    environment.draw()

def update(dt):
    for obj in environment.obj_ls:
        obj.update(dt)

dt = 1/30.
pyglet.clock.schedule_interval(update, dt) # Schedules updates for all objects every 30th of a second (Float)

body1 = body(environment,(10,15,30,25,30,10),
            (0,0,255,
            0,0,255,
            0,0,255)
            )
environment.obj_ls.append(body1)

#vertex_list = environment.obj_batch.add(2, pyglet.gl.GL_POINTS, None,
#    ('v2i', (10, 15, 30, 35)),
#    ('c3B', (0, 0, 255, 0, 255, 0))
#)


if __name__ == "__main__":
    pyglet.app.run()

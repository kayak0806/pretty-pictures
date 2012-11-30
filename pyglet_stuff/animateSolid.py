import pyglet

window = pyglet.window.Window()

class Environment(object):
    def __init__(self):
        self.obj_ls = []
        self.obj_batch = pyglet.graphics.Batch()
        
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
        
        #self.vertex_list = environment.obj_batch.add(len(points)/2,
        #    pyglet.gl.GL_POLYGON, None,
        #    ('v2f',points)
        #    )
        
        #= pyglet.graphics.vertex_list(len(points)/2,
    #('v2f', points)
    #    )
        
    def draw(self,arg=pyglet.gl.GL_POLYGON):
        self.vertex_list.draw(arg)
        
    def update(self,dt):
        for i in range(len(self.vertex_list.vertices)):
            #print self.vertex_list.vertices[i]
            self.vertex_list.vertices[i] = self.vertex_list.vertices[i] + 10

@window.event
def on_draw():
    window.clear()
    environment.obj_batch.draw()

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

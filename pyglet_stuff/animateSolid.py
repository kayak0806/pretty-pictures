'''

Simple environment/body animation code.

Environments contain a batch (obj_batch) of drawable objects (bodies) and a list (obj_ls) of objects. Environment.draw() draws everything in the environment.

bodies have an environment, contain a tuple of points (body.points) and a vertex_list (body.vertex_list, in the environment's obj_batch). body.update() applies arbitrary changes to points, then updates vertex_list to match.

update() (module level) is scheduled for every 1/30. seconds, and updates every object 

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
        
    def update(self,dt):
        for obj in self.obj_ls:
            obj.update(dt)
        
        
environment = Environment()
        
class body(object):
    
    def __init__(self,environment, points,color = None, draw_with=pyglet.gl.GL_POLYGON):
        self.draw_mode = draw_with 
        temp = pyglet.graphics.Batch()
        if color == None:
            self.vertex_list = temp.add_indexed(len(points)/2, draw_with, None, range(len(points)/2), ('v2f',points)
            )
        else:
            self.vertex_list = temp.add_indexed(len(points)/2, draw_with, None, range(len(points)/2),('v2f',points),('c3B',color)
            )
            
        self.points = points
        
        temp.migrate(self.vertex_list,self.draw_mode,
            None,environment.obj_batch)
        
        environment.obj_ls.append(self)
        
        
    # Not relevant with the current setup: we always draw from the Environment's obj_batch, which draws objects (vector lists) as they were added. This would be relevant if we wanted to draw objects individually, without calling their vector_lists. 
    def draw(self,arg=pyglet.gl.GL_POLYGON):
        self.vertex_list.draw(arg)
        
    def update(self,dt):
        points = ()
        for i in range(len(self.points)):
            #print self.vertex_list.vertices[i]
            #self.vertex_list.vertices[i] = self.vertex_list.vertices[i] + 10
            points += (self.points[i] + 20*dt,)
            
        self.points = points
        self.refresh_vertices()
        
    def refresh_vertices(self):
        self.vertex_list.vertices = self.points

@window.event
def on_draw():
    window.clear()
    environment.draw()

def update(dt):
    environment.update(dt)

dt = 1/30.
pyglet.clock.schedule_interval(update, dt) # Schedules updates for all objects every 30th of a second (Float)
'''
bod = body(environment,(10,0,10,10,0,10,0,0),
            draw_with = pyglet.gl.GL_QUADS,
            color = (0,0,255,
            0,0,255,
            0,0,255,
            0,0,255)
            )
            
bod2 = body(environment,(60,50,60,60,50,60,50,50),
            draw_with = pyglet.gl.GL_QUADS,
            color = (0,0,255,
            0,0,255,
            0,0,255,
            0,0,255)
            )
            
'''
body1 = body(environment,(10,15,20,20,30,25,30,10),
            (0,0,255,
            0,0,255,
            0,0,255,
            0,0,255)
            )


body2 = body(environment,(60,55,70,70,90,85,90,70),
            (0,0,255,
            0,0,255,
            0,0,255,
            0,0,255)
            )

#vertex_list = environment.obj_batch.add(2, pyglet.gl.GL_POINTS, None,
#    ('v2i', (10, 15, 30, 35)),
#    ('c3B', (0, 0, 255, 0, 255, 0))
#)


if __name__ == "__main__":
    pyglet.app.run()

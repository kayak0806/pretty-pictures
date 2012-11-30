import pyglet

window = pyglet.window.Window(width=400,height=400)

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
        self.points=len(self.vertex_list.vertices)
        self.dx=5
        self.dy=5
        self.changeX=False
        self.changeY=False
        
    def draw(self,arg=pyglet.gl.GL_POLYGON):
        self.vertex_list.draw(arg)
        
    def update(self,dt):
		for i in range(len(self.vertex_list.vertices)):
			if i%2==0 and (self.vertex_list.vertices[i]<0 or self.vertex_list.vertices[i]>400):
				self.changeX=True
			if i%2==1 and (self.vertex_list.vertices[i]<0 or self.vertex_list.vertices[i]>400):
				self.changeY=True
		if self.changeX==True:
			self.dx=self.dx*-1
			self.changeX=False
		if self.changeY==True:
			self.dy=self.dy*-1
			self.changeY=False
		for i in range(len(self.vertex_list.vertices)):
			if i%2==0:
				self.vertex_list.vertices[i] = self.vertex_list.vertices[i] + self.dx
			if i%2==1:
				self.vertex_list.vertices[i] = self.vertex_list.vertices[i] + self.dy

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

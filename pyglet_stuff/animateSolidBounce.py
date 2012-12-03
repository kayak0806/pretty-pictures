import pyglet
from math import *

window = pyglet.window.Window(width=500,height=400)

class Environment(object):
    def __init__(self):
        self.obj_ls = []
        self.obj_batch = pyglet.graphics.Batch()
        
environment = Environment()
        
class body(object):
    gravity=9.81
    
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
        self.dx=0
        self.dy=0
        self.centerMassX=55
        self.centerMassY=105
        self.changeX=False
        self.changeY=False
        
    def draw(self,arg=pyglet.gl.GL_POLYGON):
        self.vertex_list.draw(arg)
        
    def update(self,dt):
        if self.fixPointX!=None:
            self.dx=self.dx+9.81*atan((self.fixPointX-self.centerMassX)/(self.fixPointY-self.centerMassY))*dt
            print self.dx
        for i in range(len(self.vertex_list.vertices)):
            if i%2==0 and (self.vertex_list.vertices[i]<0 or self.vertex_list.vertices[i]>500):
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
        self.centerMassX+=self.dx
        self.centerMassY+=self.dy
         
    def fixPoint(self,x,y):
        self.fixPointX=x
        self.fixPointY=y
        
        
        
@window.event
def on_draw():
    window.clear()
    environment.obj_batch.draw()

def update(dt):
    for obj in environment.obj_ls:
        obj.update(dt)

dt = 1/60.
pyglet.clock.schedule_interval(update, dt) # Schedules updates for all objects every 60th of a second (Float)

body1 = body(environment,(50,100,50,110,60,110,60,100),
            (0,0,255,
            0,0,255,
            0,0,255,
            0,0,255)
            )
body1.fixPoint(100,150)
environment.obj_ls.append(body1)



if __name__ == "__main__":
    pyglet.app.run()

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
        self.dx=0.
        self.dy=0.
        self.centerMassX=55.
        self.centerMassY=205.
        self.changeX=False
        self.changeY=False
        self.fixPointX=None
        self.isFixed=False
        
    def draw(self,arg=pyglet.gl.GL_POLYGON):
        self.vertex_list.draw(arg)
        
    def update(self,dt):
        if self.fixPointX!=None:
            if (self.centerMassY-self.fixPointY)!=0:
                theta=atan((self.centerMassX-self.fixPointX)/(self.centerMassY-self.fixPointY))
            else:
                theta=90
            #print degrees(theta)
            CentrpAccel=(self.dx**2+self.dy**2)/self.fixLength
            self.Tempddx=(CentrpAccel*sin(theta)+self.gravity*cos(theta)*sin(theta))
            self.Tempddy=(CentrpAccel*cos(theta)-self.gravity*sin(theta)*sin(theta))
            print self.Tempddy
            #print CentrpAccel*cos(theta)
            #print self.gravity*sin(theta)*sin(theta)
            print degrees(atan(self.Tempddx/self.Tempddy))
            self.dx=self.dx+self.Tempddx*.9
            self.dy=self.dy+self.Tempddy*.9
        elif not self.isFixed:
            self.dy=self.dy-self.gravity*.1
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
        self.fixPointX=float(x)
        self.fixPointY=float(y)
        self.fixLength=sqrt((self.fixPointX-self.centerMassX)**2+(self.fixPointY-self.centerMassY)**2)
        
    def fixObject(self):
        self.isFixed=True
        
    def unFixPoint(self):
        self.fixPointX=None
        
@window.event
def on_draw():
    window.clear()
    environment.obj_batch.draw()
    
@window.event
def on_mouse_press(x,y,buttons,modifiers):
    body1.unFixPoint()

def update(dt):
    for obj in environment.obj_ls:
        obj.update(dt)
        

dt = 1/30.
pyglet.clock.schedule_interval(update, dt) # Schedules updates for all objects every 60th of a second (Float)

x=100
y=200
body1 = body(environment,(x-5,y-5,x-5,y+5,x+5,y+5,x+5,y-5),
            (0,0,255,
            0,0,255,
            0,0,255,
            0,0,255)
            )
body1.dx=1
body1.dy=1

x1=200
y1=250
body1.fixPoint(x1,y1)
#body2 = body(environment,(x1,y1,x1+10,y1,x1+10,y1+10,x1,y1+10),
#            (0,0,255,
#            0,0,255,
#            0,0,255,
#            0,0,255)
#            )
#body2.fixObject()
environment.obj_ls.append(body1)
#environment.obj_ls.append(body2)



if __name__ == "__main__":
    pyglet.app.run()

import pyglet
from math import *
from numpy import *

window = pyglet.window.Window(width=500,height=400)

class Environment(object):
    def __init__(self):
        self.obj_ls = []
        self.obj_batch = pyglet.graphics.Batch()
        
environment = Environment()
        
class body(object):
    gravity=-9.81
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
        self.centerMassX=points[0]+5
        self.centerMassY=points[1]+5
        self.vectorHor=array([1,0])
        self.vectorVer=array([0,1])
        self.changeX=False
        self.changeBottomY=False
        self.changeTopY=False
        self.fixPointX=None
        self.isFixed=False
        self.caldt=1/20.
        
    def draw(self,arg=pyglet.gl.GL_POLYGON):
        self.vertex_list.draw(arg)
        
    def update(self,dt):
        if self.fixPointX!=None:
            vectorTan=array([-(self.fixPointY-self.centerMassY),self.fixPointX-self.centerMassX])
            vectorNor=array([self.fixPointX-self.centerMassX,self.fixPointY-self.centerMassY])
            vectorTan=vectorTan/linalg.norm(vectorTan)
            vectorNor=vectorNor/linalg.norm(vectorNor)
            CentrpAccel=(self.dx**2+self.dy**2)/self.fixLength
            self.Tempddx=CentrpAccel*dot(self.vectorHor,vectorNor)+self.gravity*dot(self.vectorVer,vectorTan)*dot(self.vectorHor,vectorTan)
            self.Tempddy=CentrpAccel*dot(self.vectorVer,vectorNor)+self.gravity*dot(self.vectorVer,vectorTan)*dot(self.vectorVer,vectorTan)
            print sqrt((self.fixPointX-self.centerMassX)**2+(self.fixPointY-self.centerMassY)**2)
            self.dx=self.dx+self.Tempddx*self.caldt
            self.dy=self.dy+self.Tempddy*self.caldt
        elif not self.isFixed:
            self.dy=self.dy+self.gravity*self.caldt+-.1*self.dx*self.caldt
            self.dx=self.dx+-.1*self.dx*self.caldt
        for i in range(len(self.vertex_list.vertices)):
            if i%2==0 and (self.vertex_list.vertices[i]<0 or self.vertex_list.vertices[i]>500):
                self.changeX=True
            if i%2==1 and (self.vertex_list.vertices[i]<0):
                self.changeBottomY=True
            if i%2==1 and (self.vertex_list.vertices[i]>400):
                self.changeTopY=True
        if self.changeX==True:
            self.dx=self.dx*-1
            self.changeX=False
        if self.changeBottomY==True:
            self.dy=self.dy*-1+self.dy*.1
            self.changeBottomY=False
        if self.changeTopY==True:
            self.dy=self.dy*-1
            self.changeTopY=False
        for i in range(len(self.vertex_list.vertices)):
            if i%2==0:
                self.vertex_list.vertices[i] = self.vertex_list.vertices[i] + self.dx*self.caldt
            if i%2==1:
                self.vertex_list.vertices[i] = self.vertex_list.vertices[i] + self.dy*self.caldt
        self.centerMassX+=self.dx*self.caldt
        self.centerMassY+=self.dy*self.caldt
         
    def fixPoint(self,x,y):
        self.fixPointX=float(x)
        self.fixPointY=float(y)
        self.fixLength=sqrt((self.fixPointX-self.centerMassX)**2+(self.fixPointY-self.centerMassY)**2)
        
    def isFixedTo(self):
        if self.fixPointX!=None:
            return True
        
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
    if body1.isFixedTo():
        body1.unFixPoint()
    else:
        body1.fixPoint(x,y)

def update(dt):
    body3.fixPoint(body1.centerMassX,body1.centerMassY)
    for obj in environment.obj_ls:
        obj.update(dt)
        

dt = 1/360.
pyglet.clock.schedule_interval(update, dt) # Schedules updates for all objects every 60th of a second (Float)

x=100
y=200
body1 = body(environment,(x-5,y-5,x-5,y+5,x+5,y+5,x+5,y-5),
            (0,0,255,
            0,0,255,
            0,0,255,
            0,0,255)
            )
x1=200
y1=250
body1.fixPoint(x1,y1)
body2 = body(environment,(x1,y1,x1+10,y1,x1+10,y1+10,x1,y1+10),
            (0,0,255,
            0,0,255,
            0,0,255,
            0,0,255)
            )
body2.fixObject()
x2=50
y2=150
body3 = body(environment,(x2,y2,x2+10,y2,x2+10,y2+10,x2,y2+10),
            (0,0,255,
            0,0,255,
            0,0,255,
            0,0,255)
            )
body3.fixPoint(x,y)
environment.obj_ls.append(body1)
environment.obj_ls.append(body2)



if __name__ == "__main__":
    pyglet.app.run()

import pyglet
from math import *
from numpy import *

window = pyglet.window.Window(width=600,height=400)

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
                pyglet.gl.GL_QUADS, None,('v2f',points)
            )
        else:
            self.vertex_list = environment.obj_batch.add(len(points)/2,
                pyglet.gl.GL_QUADS, None,('v2f',points),('c3B',color)
            )
        self.points=len(self.vertex_list.vertices)
        self.dx=0.
        self.dy=0.
        self.Tempdx=0
        self.tempdy=0
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
            #print sqrt((self.fixPointX-self.centerMassX)**2+(self.fixPointY-self.centerMassY)**2)
            self.dx=self.dx+self.Tempddx*self.caldt
            self.dy=self.dy+self.Tempddy*self.caldt
            print self.Tempddy
        elif not self.isFixed:
            self.dy=self.dy+self.gravity*self.caldt+-.1*self.dx*self.caldt
            self.dx=self.dx+-.1*self.dx*self.caldt
        for i in range(len(self.vertex_list.vertices)):
            if i%2==0 and (self.vertex_list.vertices[i]<0 or self.vertex_list.vertices[i]>600):
                self.changeX=True
            if i%2==1 and (self.vertex_list.vertices[i]<0):
                self.changeBottomY=True
            if i%2==1 and (self.vertex_list.vertices[i]>400):
                self.changeTopY=True
        if self.changeX==True:
            self.dx=self.dx*-1
            self.changeX=False
        if self.changeBottomY==True:
            self.dy=self.dy*-1#+self.dy*.1
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
         
    def collision(self,other):
        self.Tempdx=other.dx
        self.Tempdy=other.dy
        other.dx=self.dx
        other.dy=self.dy
        self.dx=self.Tempdx
        self.dy=self.Tempdy

    def fixPoint(self,x,y):
        self.centerMassX=self.vertex_list.vertices[0]+5
        self.centerMassY=self.vertex_list.vertices[1]+5
        self.fixPointX=float(x)
        self.fixPointY=float(y)
        self.fixLength=sqrt((self.fixPointX-self.centerMassX)**2+(self.fixPointY-self.centerMassY)**2)
        self.dx=0
        self.dy=0
        #vectorTan=array([-(self.fixPointY-self.centerMassY),self.fixPointX-self.centerMassX])
        #vectorTan=vectorTan/linalg.norm(vectorTan)
        #self.dx=self.dx*dot(self.vectorHor,vectorTan)
        #self.dy=self.dy*dot(self.vectorVer,vectorTan)
        
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
#    if (abs(body1.centerMassX-body2.centerMassX)<3):
#        body1.collision(body2)
#    if (abs(body2.centerMassX-body3.centerMassX)<3):
#        body2.collision(body3)
#    if (abs(body1.centerMassX-body3.centerMassX)<3):
#        body1.collision(body3)
    for obj in environment.obj_ls:
        obj.update(dt)
#    print sqrt((body2.fixPointX-body2.centerMassX)**2+(body2.fixPointY-body2.centerMassY)**2)

dt = 1/10.
pyglet.clock.schedule_interval(update, dt) # Schedules updates for all objects every 60th of a second (Float)

x=200
y=100
body1 = body(environment,(x-5,y-5,x-5,y+5,x+5,y+5,x+5,y-5),
            (0,0,255,
            0,0,255,
            0,0,255,
            0,0,255)
            )
body1.fixPoint(300,200)
body1.dx=0
x1=300
y1=200
#body2 = body(environment,(x1-5,y1-5,x1-5,y1+5,x1+5,y1+5,x1+5,y1-5),
#            (0,0,255,
#            0,0,255,
#            0,0,255,
#            0,0,255)
#            )
#body2.fixObject()
#body2.fixPoint(300,300)
#body2.dx=3
#x1=400
#y1=300
#body3 = body(environment,(x1-5,y1-5,x1-5,y1+5,x1+5,y1+5,x1+5,y1-5),
#            (0,0,255,
#            0,0,255,
#            0,0,255,
#            0,0,255)
#            )
#body3.fixPoint(300,300)
environment.obj_ls.append(body1)
#environment.obj_ls.append(body2)
#environment.obj_ls.append(body3)




if __name__ == "__main__":
    pyglet.app.run()

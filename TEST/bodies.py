import pyglet
import math
from numpy import *
from calculation import *


'''Run vertexies.py'''

class Body(object):
    ''' includes move, shift, rotate, and update methods.
        set_size can be rewritten
        resize, get_points, and is_inside need to be overwritten'''

    def __init__(self, environment, x=0, y=0, heading=0, velocity = 0, density=1):
        self.environment = environment
        self.dt=1/60.
        self.heading = 0
        self.velocity = array([0.,0.])
        self.center = array([x,y])
        self.density = density
        self.color = (0,0,255,0,0,255,0,0,255,0,0,255)
        self.active = False
        self.bodyConstraints = [] # list of connected bodies
        self.freeConstraints = []
        self.track_vert = None 
    
    def track(self):
        if self.track_vert:
            self.track_points += self.get_tracked()
            if len(self.track_points)>=400*2:
                for i in range(len(self.anchors)):
                    self.track_points.pop(0)
                    self.track_points.pop(0)
            self.track_vert.resize(len(self.track_points)/2)
            self.track_vert.vertices = self.track_points
    
    def get_tracked(self):
        points = []
        for point in self.anchors:
            newx = int(self.center[0]) + int(point[0]*math.cos(point[1]))
            newy = int(self.center[1]) + int(point[0]*math.sin(point[1]))
            points += [newx, newy]
        return points

    def add_anchor(self, x,y):
        angle = self.angle(x,y)
        r = self.distance(x,y)
        if not self.track_vert:
            self.anchors = [array([r,angle])] # polar coords
            self.track_points = self.get_tracked()
            self.track_vert = self.environment.track_batch.add(len(self.track_points)/2,
                    pyglet.gl.GL_POINTS, None, ('v2f', self.track_points))
        else:
            self.anchors.append(array([r,angle]))

    def distance(self, x,y):
        xcenter = self.center[0]
        ycenter = self.center[1]
        
        return math.sqrt((xcenter - x)**2 + (ycenter-y)**2)

    def angle(self, dx, dy):
        x = float(dx - self.center[0])
        y = float(dy - self.center[1])

        return math.atan2(y,x)

    def move(self,x,y):
        self.center = array([x,y])

    def shift(self,dx,dy):
        self.center = array([self.center[0]+dx*self.dt,self.center[1]+dy*self.dt])

    def rotate(self, angle):
        self.heading = angle

    def twist(self, dangle):
        self.heading += dangle

    def joinToObject(self,body=None,fixPoint=(0,0),fixVelocity=(0,0)):
        if body!=None:
            fixDistance = math.sqrt((body.center[0]-self.center[0])**2+(body.center[1]-self.center[1])**2)
            self.bodyConstraints.append((body,fixDistance))
        else:
            fixDistance = math.sqrt((fixPoint[0]-self.center[0])**2+(fixPoint[1]-self.center[1])**2)
            self.freeConstraints.append((fixPoint,fixVelocity,fixDistance))

    def update(self,dt): 
        self.vert.vertices = self.get_points()
        if self.active:
            self.track()
            self.velocity[1]=self.velocity[1]-9.81
            for body in self.freeConstraints:
                self.velocity[0],self.velocity[1]=joinedBodies(self.center,self.velocity,body[0],body[1],body[2])
            for body in self.bodyConstraints:
                self.velocity[0],self.velocity[1]=joinedBodies(self.center,self.velocity,body[0].center,body[0].velocity,body[1])
        self.shift(self.velocity[0],self.velocity[1])
            

    def set_size(self, x, y): # can rewrite
        self.resize(x,y)
        self.vert.vertices = self.get_points()


    def resize(self,x,y): # rewrite
        pass

    def get_points(self): # rewrite
        pass

    def is_inside(self,x,y):  # rewrite
        pass


class Square(Body):
    def __init__(self, environment, x,y):
        Body.__init__(self,environment,x,y)
        self.size = 0

        points = self.get_points()
        self.color = (0,0,255)*(len(points)/2)   
        self.vert = environment.batch.add(4, pyglet.gl.GL_QUADS, None, 
                    ('v2i', points),('c3B', self.color))

    def set_size(self,x,y):
        self.resize(x,y)
        angle = self.angle(x,y)
        self.rotate(angle)
        self.vert.vertices = self.get_points()

    def resize(self,x,y):
        r = self.distance(x,y)
        self.size = r*math.sqrt(2)

    def get_points(self):
        if self.size>0:
            dx = math.cos(self.heading)*(self.size/math.sqrt(2))
            dy = math.sin(self.heading)*(self.size/math.sqrt(2))
        else:
            dx = 0
            dy = 0
        x = self.center[0]
        y = self.center[1]

        x1,y1 = x+dx, y+dy
        x2,y2 = x-dy, y+dx
        x3,y3 = x-dx, y-dy
        x4,y4 = x+dy, y-dx

        points = [x1,y1,x2,y2,x3,y3,x4,y4]
        
        for i in range(len(points)):
            points[i] = int(points[i])
        return points

    def is_inside(self,x,y):
        phi = self.angle(x,y)
        r = self.distance(x,y)
        dx = r*math.cos(phi-self.heading+math.pi/4)+self.center[0]
        dy = r*math.sin(phi-self.heading+math.pi/4)+self.center[1]
        xdist = abs(self.center[0]-dx)
        ydist = abs(self.center[1]-dy)
        return xdist <= self.size/2 and ydist <= self.size/2

class Circle(Body):
    def __init__(self, environment, x, y):
        Body.__init__(self,environment, x=x,y=y)
        self.radius = 0        
        points = self.get_points()
        self.color = (0,0,255)*(len(points)/2)
        self.vert = environment.batch.add(34, pyglet.gl.GL_TRIANGLE_STRIP, None, 
                    ('v2i', points),('c3B', self.color))

    def resize(self,x,y):
        self.radius = self.distance(x,y)
        
    def get_points(self):
        r = self.radius
        n = 30
        points = []
        for i in range(n):
            angle = 2*i*math.pi/n
            points.append(r*math.cos(angle)+self.center[0])
            points.append(r*math.sin(angle)+self.center[1])
        points = points[-2:]+points[-2:]+points+points[0:2]+points[0:2]
        for i in range(len(points)):
            points[i] = int(points[i])
        return points

    def is_inside(self,x,y):
        return self.distance(x,y) <= self.radius
    
class Rod(Body):
    def __init__(self, environment, x, y):
        Body.__init__(self,environment, x=x,y=y)
        self.width = 50
        self.length = 0

        points = self.get_points()
        self.color = (0,0,255)*(len(points)/2)   
        self.vert = environment.batch.add(4, pyglet.gl.GL_QUADS, None, 
                    ('v2i', points),('c3B', self.color))
    
    def set_size(self,x,y):
        self.resize(x,y)
        phi = math.pi/2    
        if self.length>0:
            phi = math.atan(self.width/(2*self.length))
        angle = self.angle(x,y)-phi
        self.rotate(angle)
        self.vert.vertices = self.get_points()
        

    def resize(self,x,y):
        r = self.distance(x,y)
        if r < self.width/2:
            r = self.width/2
        self.length = math.sqrt(r**2 - (self.width/2)**2)

    def get_points(self):
        dx = 0
        dy = 0
        if self.length>0:
            dx = self.length*math.cos(self.heading)
            dy = self.length*math.sin(self.heading)
        x = self.center[0]
        y = self.center[1]

        h = self.width/2 * math.sin(self.heading)
        v = self.width/2 * math.cos(self.heading)

        x1,y1 = x+dx-h, y+dy+v
        x2,y2 = x-dx-h, y-dy+v
        x3,y3 = x-dx+h, y-dy-v
        x4,y4 = x+dx+h, y+dy-v

        points = [x1,y1,x2,y2,x3,y3,x4,y4]
        
        for i in range(len(points)):
            points[i] = int(points[i])
        return points
        

    def is_inside(self,x,y):
        phi = self.angle(x,y)
        r = self.distance(x,y)
        dx = r*math.cos(phi-self.heading)+self.center[0]
        dy = r*math.sin(phi-self.heading)+self.center[1]
        xdist = abs(self.center[0]-dx)
        ydist = abs(self.center[1]-dy)
        return xdist <= self.length and ydist <= self.width/2





import pyglet
from point import Point
from copy import deepcopy
import math

'''Run vertexies.py'''

class Body(object):
    ''' includes move, shift, and rotate methods.
        update and set_size can be rewritten
        resize and get_points need to be overwritten'''

    def __init__(self, environment, x=0, y=0, heading=0, velocity = 0, density=1):
        self.environment = environment
        self.heading = 0
        self.velocity = velocity
        self.center = Point(x,y)
        self.density = density
        self.color = (0,0,255,0,0,255,0,0,255,0,0,255)
        self.active = False

    def distance(self, x,y):
        xcenter = self.center.x
        ycenter = self.center.y
        
        return math.sqrt((xcenter - x)**2 + (ycenter-y)**2)

    def angle(self, dx, dy):
        x = float(dx - self.center.x)
        y = float(dy - self.center.y)

        return math.atan2(y,x)

    def move(self,x,y):
        self.center = Point(x,y)

    def shift(self,dx,dy):
        x,y = self.center.x, self.center.y
        self.center = Point(x+dx,y+dy)

    def rotate(self, angle):
        self.heading = angle

    def twist(self, dangle):
        self.heading += dangle

    def set_size(self, x, y): # can rewrite
        self.resize(x,y)

    def update(self,dt): # can rewrite, include first two lines
        self.vert.vertices = self.get_points()
        if self.active:
            pass

    def resize(self,x,y): # rewrite
        pass

    def get_points(self): # rewrite
        pass


class Square(Body):
    def __init__(self, environment, x,y):
        Body.__init__(self,environment,x,y)
        self.size = 0
        self.heading = 0

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
            dy = math.sin(self.heading)*(self.size/math.sqrt(2)) #0.785389
        else:
            dx = 0
            dy = 0
        x = self.center.x
        y = self.center.y

        x1,y1 = x+dx, y+dy
        x2,y2 = x-dy, y+dx
        x3,y3 = x-dx, y-dy
        x4,y4 = x+dy, y-dx

        points = [x1,y1,x2,y2,x3,y3,x4,y4]
        
        for i in range(len(points)):
            points[i] = int(points[i])
        return points

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
            points.append(r*math.cos(angle)+self.center.x)
            points.append(r*math.sin(angle)+self.center.y)
        points = points[-2:]+points[-2:]+points+points[0:2]+points[0:2]
        for i in range(len(points)):
            points[i] = int(points[i])
        return points
    




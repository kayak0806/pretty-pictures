import pyglet
from point import Point
from copy import deepcopy
import math

class Body(object):
    ''' includes move and shift methods'''
    def __init__(self, environment, x=0,y=0, heading=0, velocity = 0, location=Point(0,0), density=1):
        self.environment = environment
        self.heading = 0
        self.velocity = velocity
        self.center = deepcopy(location)
        self.density = density
        self.color = (0,0,255,0,0,255,0,0,255,0,0,255)
        self.active = False
 
    def move(self,x,y):
        self.center = Point(x,y)
        self.vert.vertices = self.get_points()

    def shift(self,dx,dy):
        x,y = self.center.x, self.center.y
        self.center = Point(x+dx,y+dy)
        self.vert.vertices = self.get_points()

    def resize(self,x,y):
        pass

    def get_points(self):
        pass

    def update(self):
        pass

    def distance(self, x,y):
        xcenter = self.center.x
        ycenter = self.center.y

        return math.sqrt((xcenter - x)**2 + (ycenter-y)**2)

    def rotate(self,angle):
        pass

class Square(Body):
    def __init__(self, environment, x,y):
        Body.__init__(self,environment,location=Point(x,y))
        self.size = 0

        points = self.get_points()        
        self.vert = environment.batch.add(4, pyglet.gl.GL_QUADS, None, 
                    ('v2i', points),('c3B', self.color))

    def resize(self,x,y):
        r = self.distance(x,y)
        self.size = r*math.sqrt(2)

        self.vert.vertices = self.get_points()

    def rotate(self, angle):
        self.heading += angle
        
        self.vert.vertices = self.get_points()
    

    def update(self, dt):
#        self.vert.vertices = self.get_points()
        if self.active:
            pass

    def get_points(self):
        if self.size>0:
            dx = math.cos(self.heading+0.785389)*(self.size*math.sqrt(2))
            dy = math.sin(self.heading+0.785389)*(self.size*math.sqrt(2))
        else:
            dx = 0
            dy = 0
        x = self.center.x
        y = self.center.y

        x1,y1 = x-dx, y+dy
        x2,y2 = x-dx, y-dy
        x3, y3 = x+dx, y-dy
        x4,y4 = x+dx, y+dy

        points = [x1,y1,x2,y2,x3,y3,x4,y4]
        
        for i in range(len(points)):
            points[i] = int(points[i])
        return points

class Circle(Body):
    def __init__(self, environment, x, y):
        Body.__init__(environment, location=Point(x,y))
        self.radius = 0
        
        points = self.get_points()
        self.vert = environment.batch.add(5, pyglet.gl.GL_TRIANGLE_STRIP, None, 
                    ('v2i', points),('c3B', self.color))
        
    def get_points(self):
        r = self.radius
        points = []
        for i in range(40):
            i = i*2
            angle = i*360/20
            points[i], points[i+1] = r*math.cos(angle), r*math.sin(angle)

        for i in range(len(points)):
            points[i] = int(points[i])
        return points
    




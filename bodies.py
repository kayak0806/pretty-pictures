import pyglet
from point import Point
from copy import deepcopy
import math

class Body(object):
    def __init__(self, environment, x=0,y=0, heading=0, velocity = 0, location=Point(0,0), density=1):
        self.environment = environment
        self.heading = 0
        self.velocity = velocity
        self.center = deepcopy(location)
        self.density = density
        self.color = (0,0,255,0,0,255,0,0,255,0,0,255)
        self.active = False

    def resize(self,x,y):
        pass

    def relocate(self, location):
        self.center=location

    def get_points(self):
        pass

    def update(self):
        pass

    def distance(self, x,y):
        xcenter = self.center.x
        ycenter = self.center.y

        return sqrt((xcenter - x)**2 + (ycenter-y)**2)

    def rotate(self,angle):
        pass

class Square(Body):
    def __init__(self, enviroment, x,y):
        Body.__init__(environment,location=Point(x,y))
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

    def get_points(self):
        dx = math.cos(self.heading)/(self.size*math.sqrt(2))
        dy = math.sin(self.heading)/(self.size*math.sqrt(2))

        x = self.center.x
        y = self.center.y

        x1,y1 = x-dx, y+dy
        x2,y2 = x-dx, y-dy
        x3, y3 = x+dx, y-dy
        x4,y4 = x+dx, y+dy

        points = [x1,y1,x2,y2,x3,y3,x4,y4]
        
        for i in range(len(points)):
            points[i] = int(points[i]))
        return points
'''
class Circle(Body)
    def __init__(self, environment, x, y):
        Body.__init__(environment, location=Point(x,y))
        self.radius = 0
        
        points = self.get_points()
        self.vert = environment.batch.add(5, pyglet.gl.GL_TRIANGLE_STRIP, None, 
                    ('v2i', points),('c3B', self.color))
        
    def get_points(self):
        points = []
        for angle in range(60)*6:
            




'''

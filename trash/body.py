'''
Creates a body that stores:
    center point
    size
    density
    mass
'''
import pyglet
import numpy
from environment import Environment
from point import Point

class Body(object):
    #def __init__(self, center_point, size, shape, density=1):
    #    self.center=center_point    # point
    #    self.size = size            # list of sizes (eg. [radius] or [x, y])    
    #    self.shape = shape          # string indicating shape (circle or rectangle for now)
    #    self.density = density            # density, default 1
    #    self.mass = self.area(size) * self.density # mass, based on area and density
    def __init__(self,environment, points,color = None):
    '''
    points is a list of Point objects
    '''
        if color == None:
            self.vertex_list = environment.obj_batch.add(len(points)/2,
                pyglet.gl.GL_POLYGON, None,('v2f',points)
            )
        else:
            self.vertex_list = environment.obj_batch.add(len(points)/2,
                pyglet.gl.GL_POLYGON, None,('v2f',points),('c3B',color)
            )
            
        self.points = points
        
        environment.obj_ls.append(self)
        
    def com(self):
        com = sum(self.points)/(self.density*len(points)
        
    def update(self,dt):
        points = ()
        for i in range(len(self.points)):
            #print self.vertex_list.vertices[i]
            #self.vertex_list.vertices[i] = self.vertex_list.vertices[i] + 10
            points += (self.points[i] + 10,)
            
        self.points = points
        self.refresh_vertices()
        
    def refresh_vertices(self):
        self.vertex_list.vertices = self.points
        


class circleShape(Body):
    def __init__(self, center_point, size, density=1):
        self.center=center_point    # point
        self.radius = size[0]       # radius
        self.p = density            # density, default 1
        self.mass = self.area(self.radius) * self.p # mass, based on area and density
    
    def area(self, raduis):
        return r**2 * 3.14159

'''
class rectShape(Body):
    def __init__(self, center_point, size, density=1):
        self.center=center_point    # point
        self.width = size[0]        # width
        self.height = size[1]       # height
        self.p = density            # density, default 1
        self.mass = self.area(self.width, self.height) * self.p # mass, based on area and density
    
    def area(self, width, height):
        return width * height

p1 = Point([0,0],[0,0],[0,0],[0,0])
p2 = Point([5,5],[0,0],[0,0],[0,0])

b = Body([p1,p2])
'''

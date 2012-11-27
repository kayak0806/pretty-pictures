'''
Creates a body that stores:
    center point
    size
    density
    mass
'''

imporrt pyglet
from point import Point

class Body(pyglet.sprite.Sprite): # Using the Sprite class will let us animate objects with pyglet using Sprite.Update(). See: http://pyglet.org/doc/programming_guide/noisy.py
    def __init__(self, center_point, size, shape, density=1):
        self.center=center_point    # point
        self.size = size            # list of sizes (eg. [radius] or [x, y])    
        self.shape = shape          # string indicating shape (circle or rectangle for now)
        self.p = density            # density, default 1
        self.mass = self.area(size) * self.p # mass, based on area and density


class circleShape(Body):
    def __init__(self, center_point, size, density=1):
        self.center=center_point    # point
        self.radius = size[0]       # radius
        self.p = density            # density, default 1
        self.mass = self.area(self.radius) * self.p # mass, based on area and density
    
    def area(self, raduis):
        return r**2 * 3.14159

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



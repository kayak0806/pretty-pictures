'''
Creates a body that stores:
    defining points
    density
    mass
'''

imporrt pyglet
from point import Point

class Body(pyglet.sprite.Sprite): # Using the Sprite class will let us animate objects with pyglet using Sprite.Update(). See: http://pyglet.org/doc/programming_guide/noisy.py
    def __init__(self, def_points, density=1):
        self.def_points=def_points
        self.p = density
        self.mass = self.area(def_points)


    def area(self,points):
        a = 0
        last = points[-1]
        for point.car_position in Points:
            print last



p1 = Point([0,0],[0,0],[0,0],[0,0])
p2 = Point([5,5],[0,0],[0,0],[0,0])

b = Body([p1,p2])



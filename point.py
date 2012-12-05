'''
Creates points that stores
    Cartesian position
    Rotation position
    Cartesian velocity
    Rotation velocity
'''
import pyglet

class Point(object):
    def __init__(self,x=0,y=0,z=0):
        self.x = x
        self.y = y
        self.z = z
        
    def __print__(self):
        return "(%.2d,%.2d,%.2d)"%(self.x,self.y,self.z)
        
    def __add__(self,other):
        return Point(self.x + other.x,self.y + other.y,self.z + other.z)

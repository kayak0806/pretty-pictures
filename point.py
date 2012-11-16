'''
Creates points that stores
    Cartesian position
    Rotation position
    Cartesian velocity
    Rotation velocity
'''
import pyglet

class Point(pyglet.sprite.Sprite): # Using the Sprite class will let us animate objects with pyglet using Sprite.Update(). See: http://pyglet.org/doc/programming_guide/noisy.py
    def __init__(self,car_position,rot_position,car_velocity,rot_velocity):
        self.car_position=car_position      # list [x,y,z]
        self.rot_position=rot_position      # yaw or list [yaw, pitch, roll]
        self.car_velocity=car_velocity      # list [x,y,z]
        self.rot_velocity=rot_velocity	    # yaw or list [yaw, pitch, roll]
		

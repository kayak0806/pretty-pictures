'''
Creates points that stores
    Cartesian position
    Rotation position
    Cartesian velocity
    Rotation velocity
'''
class Point(object):
    def __init__(self,car_position,rot_position,car_velocity,rot_position):
        self.car_position=car_position      # list [x,y,z]
        self.rot_position=rot_position      # yaw or list [yaw, pitch, roll]
        self.car_velocity=car_velocity      # list [x,y,z]
        self.rot_velocity=rot_velocity	    # yaw or list [yaw, pitch, roll]
		

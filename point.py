'''
Creates points that stores
	Cartesian position
	Rotation position
	Cartesian velocity
	Rotation velocity
'''
class Point(object):
	def __init__(self,car_position,rot_position,car_velocity,rot_position):
		self.car_position=car_position
		self.rot_position=rot_position
		self.car_velocity=car_velocity
		self.rot_velocity=rot_velocity	
		

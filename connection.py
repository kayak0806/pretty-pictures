'''
Creates connections between points
'''
class Connection(object):
    def __init__(self,point1,point2):
        self.connection_point1=point1
        self.connection_point2=point2
        
    def absolute_distance(self):
        '''
        This finds the normal distance between two points
        '''
        return ((connection_point1[0]-connection_point2[0])**2+(connection_point1[1]-connection_point2[1])**2)**.5

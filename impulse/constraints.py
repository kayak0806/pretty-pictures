from bodies import *
from math import *

class constraints(object):
    def __init__(self,body1=None,body2=None,center=(0,0)):
        self.body1=body1
        self.body2=body2
        self.center=center
        if center==(0,0):
            self.fixLength=sqrt((self.body1.center[0]-self.body2.center[0])**2+(self.body1.center[1]-self.body2.center[1])**2)
        else:
            self.fixLength=sqrt((body1.center[0]-center[0])**2+(body1.center[1]-center[1])**2)
        

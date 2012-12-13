from numpy import *

def gravity(center,velocity):
    return (0,-98.1)

def Centrp(center,velocity,fixLength,fixCenter):
    vectorHor=array([1,0])
    vectorVer=array([0,1])
    vectorTan=array([-(fixCenter[1]-center[1]),fixCenter[0]-center[0]])
    vectorNor=array([fixCenter[0]-center[0],fixCenter[1]-center[1]])
    vectorTan=vectorTan/linalg.norm(vectorTan)
    vectorNor=vectorNor/linalg.norm(vectorNor)
    CentrpAccel=(velocity[0]**2+velocity[1]**2)/fixLength
    ddx=CentrpAccel*dot(vectorHor,vectorNor)+98.1*dot(vectorVer,vectorNor)*dot(vectorHor,vectorNor)
    ddy=CentrpAccel*dot(vectorVer,vectorNor)+98.1*dot(vectorVer,vectorNor)*dot(vectorVer,vectorNor)
    return (ddx,ddy)

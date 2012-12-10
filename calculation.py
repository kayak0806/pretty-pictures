from numpy import *

def gravity(center,velocity):
    return (0,0)

def Centrp(center,velocity,fixLength,fixCenter):
    vectorHor=array([1,0])
    vectorVer=array([0,1])
    vectorTan=array([-(fixCenter[1]-center[1]),fixCenter[0]-center[0]])
    vectorNor=array([fixCenter[0]-center[0],fixCenter[1]-center[1]])
    vectorTan=vectorTan/linalg.norm(vectorTan)
    vectorNor=vectorNor/linalg.norm(vectorNor)
    CentrpAccel=(velocity[0]**2+velocity[1]**2)/fixLength
    ddx=CentrpAccel*dot(vectorHor,vectorNor)-9.81*dot(vectorVer,vectorTan)*dot(vectorHor,vectorTan)
    ddy=CentrpAccel*dot(vectorVer,vectorNor)-9.81*dot(vectorVer,vectorTan)*dot(vectorVer,vectorTan)
    return (ddx,ddy)

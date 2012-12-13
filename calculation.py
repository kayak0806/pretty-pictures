from numpy import *

def joinedBodies(selfCenter=0,selfVelocity=0,otherBody=0,otherCenter=0,otherVelocity=0,fixedDistance=0):
    if otherBody!=0:
        vectorHor=array([1,0])
        vectorVer=array([0,1])
        vectorTan=array([-(otherBody.center[1]-selfCenter[1]),otherBody.center[0]-selfCenter[0]])
        vectorNor=array([otherBody.center[0]-selfCenter[0],otherBody.center[1]-selfCenter[1]])
        vectorTan=vectorTan/linalg.norm(vectorTan)
        vectorNor=vectorNor/linalg.norm(vectorNor)
        tempDis=math.sqrt((otherBody.center[0]-selfCenter[0])**2+(otherBody.center[1]-selfCenter[1])**2)
        disError=fixedDistance-tempDis
        dx=selfVelocity[0]-dot(selfVelocity,vectorNor)*dot(vectorHor,vectorNor)+dot(otherBody.velocity,vectorNor)*dot(vectorHor,vectorNor)-10*disError*dot(vectorHor,vectorNor)
        dy=selfVelocity[1]-dot(selfVelocity,vectorNor)*dot(vectorVer,vectorNor)+dot(otherBody.velocity,vectorNor)*dot(vectorVer,vectorNor)-10*disError*dot(vectorVer,vectorNor)
        otherBody.velocity[0]=otherBody.velocity[0]-dot(selfVelocity,vectorNor)*dot(vectorHor,vectorNor)
        otherBody.velocity[1]=otherBody.velocity[1]-dot(selfVelocity,vectorNor)*dot(vectorVer,vectorNor)
        print dot(selfVelocity,vectorNor)*dot(vectorVer,vectorNor)
        return (dx,dy)
    else:   
        vectorHor=array([1,0])
        vectorVer=array([0,1])
        vectorTan=array([-(otherCenter[1]-selfCenter[1]),otherCenter[0]-selfCenter[0]])
        vectorNor=array([otherCenter[0]-selfCenter[0],otherCenter[1]-selfCenter[1]])
        vectorTan=vectorTan/linalg.norm(vectorTan)
        vectorNor=vectorNor/linalg.norm(vectorNor)
        tempDis=math.sqrt((otherCenter[0]-selfCenter[0])**2+(otherCenter[1]-selfCenter[1])**2)
        disError=fixedDistance-tempDis
        dx=selfVelocity[0]-dot(selfVelocity,vectorNor)*dot(vectorHor,vectorNor)+dot(otherVelocity,vectorNor)*dot(vectorHor,vectorNor)-10*disError*dot(vectorHor,vectorNor)
        dy=selfVelocity[1]-dot(selfVelocity,vectorNor)*dot(vectorVer,vectorNor)+dot(otherVelocity,vectorNor)*dot(vectorVer,vectorNor)-10*disError*dot(vectorVer,vectorNor)
        return (dx,dy)

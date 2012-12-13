from numpy import *

def joinedBodies(firstBody=None,secondBody=None,fixPoint=(0,0),fixedDistance=0):
    if secondBody!=None:
        vectorHor=array([1,0])
        vectorVer=array([0,1])
        vectorTan=array([-(secondBody.center[1]-firstBody.center[1]),secondBody.center[0]-firstBody.center[0]])
        vectorNor=array([secondBody.center[0]-firstBody.center[0],secondBody.center[1]-firstBody.center[1]])
        vectorTan=vectorTan/linalg.norm(vectorTan)
        vectorNor=vectorNor/linalg.norm(vectorNor)
        tempDis=math.sqrt((secondBody.center[0]-firstBody.center[0])**2+(secondBody.center[1]-firstBody.center[1])**2)
        disError=fixedDistance-tempDis
        temp1x=dot(firstBody.velocity,vectorNor)*dot(vectorHor,vectorNor)-dot(secondBody.velocity,vectorNor)*dot(vectorHor,vectorNor)+10*disError*dot(vectorHor,vectorNor)
        temp1y=dot(firstBody.velocity,vectorNor)*dot(vectorVer,vectorNor)-dot(secondBody.velocity,vectorNor)*dot(vectorVer,vectorNor)+10*disError*dot(vectorVer,vectorNor)
        temp2x=dot(secondBody.velocity,vectorNor)*dot(vectorHor,vectorNor)-dot(firstBody.velocity,vectorNor)*dot(vectorHor,vectorNor)+10*disError*dot(vectorHor,vectorNor)
        temp2y=dot(secondBody.velocity,vectorNor)*dot(vectorVer,vectorNor)-dot(firstBody.velocity,vectorNor)*dot(vectorVer,vectorNor)+10*disError*dot(vectorVer,vectorNor)
        firstBody.velocity[0]=firstBody.velocity[0]-temp1x
        firstBody.velocity[1]=firstBody.velocity[1]-temp1y
        secondBody.velocity[0]=secondBody.velocity[0]-temp2x
        secondBody.velocity[1]=secondBody.velocity[1]-temp2y
    else:   
        vectorHor=array([1,0])
        vectorVer=array([0,1])
        vectorTan=array([-(fixPoint[1]-firstBody.center[1]),fixPoint[0]-firstBody.center[0]])
        vectorNor=array([fixPoint[0]-firstBody.center[0],fixPoint[1]-firstBody.center[1]])
        vectorTan=vectorTan/linalg.norm(vectorTan)
        vectorNor=vectorNor/linalg.norm(vectorNor)
        tempDis=math.sqrt((fixPoint[0]-firstBody.center[0])**2+(fixPoint[1]-firstBody.center[1])**2)
        disError=fixedDistance-tempDis
        firstBody.velocity[0]=firstBody.velocity[0]-dot(firstBody.velocity,vectorNor)*dot(vectorHor,vectorNor)-10*disError*dot(vectorHor,vectorNor)
        firstBody.velocity[1]=firstBody.velocity[1]-dot(firstBody.velocity,vectorNor)*dot(vectorVer,vectorNor)-10*disError*dot(vectorVer,vectorNor)

''' for testing random things'''


import pyglet
from bodies import Body
from point import Point
import math

window = pyglet.window.Window()
batch = pyglet.graphics.Batch()




x1, y1 = 300,200
x2, y2 = 200, 200

x3, y3 = 286,249

line = (x1,y1,x2,y2,x3,y3)
x = (x3-x2)
y = float(y3-y2)
angle = math.pi/6
print math.tan(angle)

if y>=0:
    if x ==0:
        theta = math.pi/2
    elif x > 0:
        theta = math.atan(y/x)
    elif x < 0:
        theta = math.atan(y/x)+math.pi
elif y<0:
    if x ==0:
        theta = math.pi+math.pi/2
    elif x > 0:
        theta = math.atan(y/x)+2*math.pi
    elif x < 0:
        theta = math.atan(y/x)+math.pi

print theta, angle
print x,y
print math.tan(0)

batch.add(2, pyglet.gl.GL_LINES, None,('v2i', line[:4]))
batch.add(2, pyglet.gl.GL_LINES, None,('v2i', line[2:]))


@window.event
def on_draw():
    window.clear()
    batch.draw()



pyglet.app.run()







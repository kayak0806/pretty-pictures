import pyglet
from pyglet.window import mouse

window = pyglet.window.Window()


batch = pyglet.graphics.Batch()

batchlist = []
squares = []


class Square(object):
    ''' A square has a location (x,y), a side length, and 
                the square's location within the batchlist'''
    def __init__(self,x,y):
        self.x1 = x
        self.y1 = y
        self.x2 = x
        self.y2 = y
        points = self.get_points()
        self.vert = batch.add(4, pyglet.gl.GL_QUADS, None, ('v2i', points))
        batchlist.append(self.vert)

    def resize(self,x,y):
        #vert = batchlist[self.index]
        self.vert.vertices[0:2] = [x,y]
        self.vert.vertices[2] = x
        self.vert.vertices[-1] = y

    def relocate(self,x,y):
        self.vert.vertices[0:2] = [x,y]
	    
    def get_points(self):
        left = self.x1
        right = self.x2
        top = self.y1
        bottom = self.y2
        return (left,top,left,bottom,right,bottom,right,top)
        # (top left), (bottom left), (bottom right), (top right)

class Triangle(object):
    ''' A Triangle has a centerpoint, a cornerpoint and a vert_list'''
    def __init__(self,x,y):
        self.xcenter = x
        self.ycenter = y
        self.xcorner = x
        self.ycorner = y
        points = self.get_points()
        self.vert = batch.add(4, pyglet.gl.GL_TRIANGLES, None, ('v2i', points))
        batchlist.append(self.vert)

    def resize(self,x,y):
        self.xcorner = x
        self.ycorner = y
        points = self.get_points()
        self.vert.verticies = points

    def relocate(self,x,y):
        self.vert.vertices[0:2] = [x,y]
	    
    def get_points(self):
        s = ((self.xcenter-self.xcorner)**2 + (self.ycenter-self.ycorner)**2)**.5
        topx = self.xcenter
        topy = self.ycenter + 10
        leftx = self.xcenter
        lefty = self.ycenter
        rightx = self.xcorner
        righty = self.ycorner
        return (topx, topy, leftx, lefty, rightx, righty, topx, topy)
    

@window.event
def on_draw():
    window.clear()
    batch.draw()

@window.event
def on_mouse_press(x, y, button, modifiers):
    squares.append(Triangle(x,y))
        
@window.event
def on_mouse_drag(x, y, dx,dy,button, modifiers):
    squares[-1].resize(x,y)

@window.event
def on_mouse_release(x, y, button, modifiers):
    last = len(squares)
   # if last > 1:    
    #    squares[last-2].relocate(0,0)

pyglet.app.run()


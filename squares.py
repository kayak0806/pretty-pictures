import pyglet


class Square(object): #blue square
    ''' A blue Square'''
    def __init__(self,environment=None,x,y):
        self.envi = environment
        self.velocity = -1
        self.active = False
        self.vert1 = x
        self.hznt1 = y
        self.vert2 = x
        self.hznt2 = y
        if enviroment:
            points = self.get_points()
            self.vert = environment.batch.add(4, pyglet.gl.GL_QUADS, None, 
                        ('v2i', points),('c3B', (0,0,255,0,0,255,0,0,255,0,0,255)))

    def resize(self,x,y):
        ''' changes the size of the square by moving p1 to (x,y)'''
        self.vert2 = x
        self.hznt2 = y
        self.vert.vertices = self.get_points()

    def relocate(self,x,y):
        ''' moves the first point to (x,y)'''
        self.vert1 = x
        self.hznt1 = y
        self.vert.vertices = self.get_points()
	    
    def get_points(self):
        ''' Given the defining points, return tuple to make vertex_list'''
        x1, y1 = self.vert1, self.hznt1
        x2, y2 = self.vert2, self.hznt1

        x3, y3 = self.vert2, self.hznt2
        x4, y4 = self.vert1, self.hznt2

        return (int(x1), int(y1), int(x2), int(y2), int(x3), int(y3), int(x4), int(y4))

    def update(self,dt):
        if self.active:
            dy = dt*30*self.velocity
            if self.hznt2 < 0 or self.hznt1 < 0:
                self.velocity = 1
            if self.hznt2 > 400 or self.hznt1>500:
                self.velocity = -1
            self.hznt1 += dy
            self.hznt2 += dy
            points = self.get_points()
            self.vert.vertices = points

class Square2(Square):
    def __init__(self,environment,x,y):
        Square.__init__(self, environment, x,y)
        points = self.get_points()
        self.vert = environment.batch.add(4, pyglet.gl.GL_QUADS, None, ('v2i', points))
        
    def update(self,dt):
        if self.active:
            dy = dt*30*self.velocity
            if self.vert2 < 0 or self.vert1 < 0:
                self.velocity = 1
            if self.vert2 > 400 or self.vert1>700:
                self.velocity = -1
            self.vert1 += dy
            self.vert2 += dy
            points = self.get_points()
            self.vert.vertices = points


import pyglet


class Button(object):
    def __init__(self, environment, x, y, text = 'button'):
        self.active = False
        self.color = 'blue' 
        self.x = x
        self.y = y
        self.text = text
        points = self.get_points()
        self.box_vert = environment.button_batch.add(4, pyglet.gl.GL_QUADS, None, 
                    ('v2i', points),('c3B', (0,0,255,0,0,255,0,0,255,0,0,255)))
        self.text_vert = pyglet.text.Label(self.text,
                          font_name='Times New Roman',
                          font_size=20,
                          color=(0, 0, 0, 255),
                          x=self.x, y=self.y,
                          anchor_x='center', anchor_y='center',
                          batch = environment.button_batch)
    def update(self,dt):
        if self.active:
            if self.color == 'blue':
                self.color = 'white'
                self.active = False
                self.box_vert.colors = [255,255,255]*4
            elif self.color == 'white':
                self.color = 'blue'
                self.box_vert.colors = [0,0,255]*4
                self.active = False


    def get_points(self):
        width = 100
        height = 50

        x1, y1 = self.x - width/2, self.y + height/2
        x2, y2 = self.x - width/2, self.y - height/2
        x3, y3 = self.x + width/2, self.y - height/2
        x4, y4 = self.x + width/2, self.y + height/2

        return (int(x1), int(y1), int(x2), int(y2), int(x3), int(y3), int(x4), int(y4))

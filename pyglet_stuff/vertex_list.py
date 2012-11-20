import pyglet

window = pyglet.window.Window()

vertex_list = pyglet.graphics.vertex_list(1024, 'v3f', 'c4B', 't2f', 'n3f')
#vertex_list = pyglet.graphics.vertex_list(2,
#    ('v2i', (10, 15, 30, 35)),
#    ('c3B', (0, 0, 255, 0, 255, 0))
#)

@window.event
def on_draw():
    window.clear()
    vertex_list.draw(pyglet.gl.GL_POINTS)
    
pyglet.app.run()

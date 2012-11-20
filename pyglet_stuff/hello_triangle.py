import pyglet

window = pyglet.window.Window()

@window.event
def on_draw():
    window.clear()
    #pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES,
    #[0, 1, 2, 0, 2, 3],
    #('v2i', (100, 100,
    #         150, 100,
    #         150, 150,
    #         100, 150))
    pyglet.graphics.draw_indexed(3, pyglet.gl.GL_TRIANGLES,
    [0, 1, 2],
    ('v2i', (100, 100,
             150, 100,
             150, 150))
    
    )
    
pyglet.app.run()

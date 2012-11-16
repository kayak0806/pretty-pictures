import pyglet
from pyglet.window import mouse

window = pyglet.window.Window()

label = pyglet.text.Label('Hello, world',
                        font_name='Times New Roman',
                        font_size=36,
                        x = window.width//2, y=window.height//2,
                        anchor_x='center', anchor_y='center')
                        
# "As with the image loading example presented earlier, pyglet.resource.media locates the sound file in the application's directory (not the working directory). If you know the actual filesystem path (either relative or absolute), use pyglet.media.load."

# "Short sounds, such as a gunfire shot used in a game, should be decoded in memory before they are used, so that they play more immediately and incur less of a CPU performance penalty. Specify streaming=False in this case:
#   sound = pyglet.resource.media('shot.wav', streaming=False)"
image = pyglet.resource.image('kitten.jpg')

music = pyglet.resource.media('music.mp3')
music.play()

@window.event
def on_key_press(symbol, modifiers): #The key symbols are defined in pyglet.window.key
    if symbol >= 0 and symbol <= 257:
        if modifiers == 17:
            print "The \'%s\' key was pressed." % chr(symbol).upper()
        else:
            print "The \'%s\' key was pressed." % chr(symbol)

@window.event
def on_mouse_press(x,y,button,modifiers): #The x and y parameters give the position of the mouse when the button was pressed, relative to the lower-left corner of the window.
    if button == mouse.LEFT:
        print "THE LEFT MOUSE BUTTON WAS PRESSED."

@window.event
def on_draw():
    window.clear()
    image.blit(0,0)
    
window.push_handlers(pyglet.window.event.WindowEventLogger()) #prints all events received on the window to the console
pyglet.app.run()

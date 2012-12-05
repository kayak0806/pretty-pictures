from Tkinter import *

root = Tk()

class Square(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = 'red'
        self.thing = Label(body,text='square', bg=self.get_color())

    def set_color(self, color):
        self.color = color
        self.thing.bg=self.color
    
    def get_color(self):
        return self.color



body = Frame(width=150, height=400, bg="#225500")

sq = Square(50, 100)

color = Button(body, text='blue', command=lambda: sq.set_color('blue'))



body.grid(row=0, column=0, sticky=N+S)
sq.thing.pack()
color.pack()

root.mainloop()

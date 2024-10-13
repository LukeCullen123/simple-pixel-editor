from tkinter import *
from tkinter.colorchooser import askcolor
import os

PIXEL_SIZE = 20

WIDTH = 1000
HEIGH = 1000
WHITE = "#ffffff"
BLACK = "#000000"

class Pixel:
    def __init__(self,x,y) -> None:
        self.color = WHITE
        self.pos = [x,y]
        
        self.square = canvas.create_rectangle(
            self.pos[0],self.pos[1], self.pos[0]+PIXEL_SIZE, self.pos[1]+PIXEL_SIZE, fill=self.color
        )

    def changecolor(self) -> None: 
        self.color = brush_color[1]
        canvas.delete(self.square)
        self.square = canvas.create_rectangle(
            self.pos[0],self.pos[1], self.pos[0]+PIXEL_SIZE, self.pos[1]+PIXEL_SIZE, fill=self.color
        )
    
    def rubber(self):
        self.square = canvas.create_rectangle(
            self.pos[0],self.pos[1], self.pos[0]+PIXEL_SIZE, self.pos[1]+PIXEL_SIZE, fill=WHITE
        )




def change_color():
    global brush_color
    global rubber 
    rubber = False
    brush_color = askcolor(title="Tkinter Color Chooser")


def brush():
    """
    Make the pixel click put down color
    """
    global brush_color
    global rubber 
    rubber = False
    brush_color = brush_color

  

def Rubber():
    """
    Make the pixel click remove color
    """
    global rubber
    rubber = True




def click(x,y):
    global rubber
    
    pos= [(x//PIXEL_SIZE)*PIXEL_SIZE, (y//PIXEL_SIZE)*PIXEL_SIZE]
    try:
        tile = box[str(pos)]
        if rubber:
            tile.rubber()
        else:
            tile.changecolor()
    except:
        pass

    
def clearall():
    for i in box:
        tile=box[i]
        tile.rubber()

    




def getorigin(eventorigin):
      global x,y
      x = eventorigin.x
      y = eventorigin.y
      #print(x,y)
      click(x,y)



window = Tk() # init window
window.title("PixelPainter") #set the the title of the window 
window.resizable(False, False) # make the window not able to be resize


brush = Button(window,text="Brush",command=brush,width=(50)) # brush button init when click go to the bruch function 
rubber = Button(window,text="rubber",command=Rubber,width=(50))# rubber button init when click go to the rubber function 
Change = Button(window,text="Change Color",command=change_color,width=(50)) # brush button init when click go to the bruch function
Clear = Button(window,text="Clear All",command=clearall,width=(50)) 
brush.grid(row=1, column=0)
Change.grid(row=2,column=0)
rubber.grid(row=1, column=1)
Clear.grid(row=2,column=1)
 


canvas = Canvas(window, bg=WHITE, height=HEIGH, width=WIDTH)
canvas.grid(row=3, column=0,columnspan=2)
canvas.bind("<B1-Motion>",getorigin)





brush_color = ["",BLACK]
rubber = False
box = {}
for x in range(WIDTH // PIXEL_SIZE):
    for y in range(HEIGH // PIXEL_SIZE):
        pixel = Pixel(x*PIXEL_SIZE,y*PIXEL_SIZE)
        box[str(pixel.pos)] = pixel

window.mainloop()


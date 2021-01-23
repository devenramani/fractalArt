from tkinter import *

import turtle

from fractalDesignHandler import fractalDesignHandler

def drawFractal(fractal):
    #print(fractal)
    fd = fractalDesignHandler(fractal)
    fd.draw(turtle)
 
fractalWindow = Tk()
fractalWindow.title("Fractal Designer")
fractalWindow.geometry('325x250')
fractalWindow.configure(background = "gray")

SnowflakeButton = Button(fractalWindow, text = "Snowflake", command = lambda: drawFractal("Snowflake"))
TreeButton = Button(fractalWindow, text = "Tree", command = lambda: drawFractal("Tree"))
StarButton = Button(fractalWindow, text = "Star", command = lambda: drawFractal("Star"))
SpiralStarButton = Button(fractalWindow, text = "SpiralStar", command = lambda: drawFractal("SpiralStar"))

SnowflakeButton.place(x = 35,y = 30)
TreeButton.place(x = 35, y = 60)
StarButton.place(x = 35, y = 90)
SpiralStarButton.place(x = 35, y = 120)

fractalWindow.mainloop()


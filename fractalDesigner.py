from tkinter import *
from tkinter import messagebox

from fractalDesign import fractalDesign

def drawFractal():
    fd = fractalDesign("Snowflake")
    fd.draw()
 
fractalWindow = Tk()
fractalWindow.title("Fractal Designer")
fractalWindow.geometry('325x250')
fractalWindow.configure(background = "gray")

F1 = Button(fractalWindow, text = "Fractal1", command = drawFractal)
F1.place(x = 35,y = 50)

fractalWindow.mainloop()


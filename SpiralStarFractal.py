from fractalDesign import fractalDesign

class SpiralStar(fractalDesign):
    
    def __init__(self):
        print("initializing SpiralStar")

    #code ref https://www.geeksforgeeks.org/draw-spiraling-star-using-turtle-in-python/?ref=rp
    def draw(self, turtle):
        sides = 30
        
        t = turtle.Turtle() 
        t.goto((150,150)) 
        t.speed(60)
        t.color('Orange')

        for i in range(sides): 
            t.forward(i * 10) 
            t.right(144) 
    
        turtle.done() 
    



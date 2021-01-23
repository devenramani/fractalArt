from fractalDesign import fractalDesign

class Star(fractalDesign):
    
    def __init__(self):
        print("initializing Star")

    #code ref https://www.geeksforgeeks.org/star-fractal-printing-using-turtle-in-python/
    def draw(self, turtle):
        def star(turtle, size): 
            if size <= 10: 
                return
            else: 
                for i in range(5): 
                    turtle.forward(size) 
                    star(turtle, size/3) 
                    turtle.left(216) 
        
        t = turtle.Turtle()  
        t.goto((-200,200)) 
        t.speed(60)
        t.color('Red')

        star(t, 120) 
        turtle.done() 

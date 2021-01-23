from fractalDesign import fractalDesign

class Snowflake(fractalDesign):

    def __init__(self):
        print("initializing SnowFlake")

    #code ref https://towardsdatascience.com/creating-fractals-with-python-d2b663786da6
    def draw(self, turtle):
        def koch_curve(t, iterations, length, shortening_factor, angle):
            if iterations == 0:
                t.forward(length)
            else:
                iterations = iterations - 1
                length = length / shortening_factor
                koch_curve(t, iterations, length, shortening_factor, angle)
                t.left(angle)
                koch_curve(t, iterations, length, shortening_factor, angle)
                t.right(angle * 2)
                koch_curve(t, iterations, length, shortening_factor, angle)
                t.left(angle)
                koch_curve(t, iterations, length, shortening_factor, angle)
        
        t = turtle.Turtle()
        t.goto((120, -120)) 
        t.speed(60)
        t.color('blue')

        for i in range(3):
            koch_curve(t, 3, 200, 3, 60)
            t.right(120)
        turtle.mainloop()
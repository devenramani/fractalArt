from fractalDesign import fractalDesign

class Tree(fractalDesign):

    MINIMUM_BRANCH_LENGTH = 5

    def __init__(self):
        print("initializing Tree")

    #code ref https://towardsdatascience.com/creating-fractals-with-python-d2b663786da6
    def draw(self, turtle):
        def build_tree(t, branch_length, shorten_by, angle):
            if(branch_length > self.MINIMUM_BRANCH_LENGTH):
                t.forward(branch_length)
                new_length = branch_length - shorten_by

                t.left(angle)
                build_tree(t, new_length, shorten_by, angle)

                t.right(angle * 2)
                build_tree(t, new_length, shorten_by, angle)

                t.left(angle)
                t.backward(branch_length)

        t = turtle.Turtle()
        t.goto((-200, -200)) 
        t.speed(200)
        t.color('green')
        t.setheading(90)
        
        build_tree(t, 50, 5, 30)
        turtle.mainloop()
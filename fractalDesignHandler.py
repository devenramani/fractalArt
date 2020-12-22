from Snowflake import Snowflake
from Tree import Tree

class fractalDesignHandler:

    fractalDesign = ""

    def __init__(self, fractalDesign):
        self.fractalDesign = fractalDesign
        
    def draw(self, turtle):
        print(self.fractalDesign)

        if(self.fractalDesign == "Snowflake"):
            sf = Snowflake()
            sf.draw(turtle)
            
        elif(self.fractalDesign == "Tree"):
            t = Tree()
            t.draw(turtle)

        else:
            print("no fractal selected")
        
        
        
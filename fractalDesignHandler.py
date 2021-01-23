from SnowflakeFractal import Snowflake
from TreeFractal import Tree
from StarFractal import Star
from SpiralStarFractal import SpiralStar

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

        elif(self.fractalDesign == "Star"):
            t = Star()
            t.draw(turtle)

        elif(self.fractalDesign == "SpiralStar"):
            t = SpiralStar()
            t.draw(turtle)

        else:
            print("no fractal selected")
        
        
        
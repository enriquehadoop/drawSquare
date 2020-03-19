class clsSquare:
    str1=" "
    str2="*"

    def __init__(self,side):    
        self.side = (side)


    def printBase(self):
        print(self.str2 * int(self.side))
    def printSide(self):
        for i in range(self.side):
            print(self.str2 * 1 + self.str1 * (self.side-2) + self.str2 * 1)
    def builSquare(self):
        res = isinstance(self.side, str) 
        

        if res!=True:
            self.printBase()
            self.printSide()
            self.printBase()
        elif res==True:
            print("Value its String or char")
        else:
            print("Value must be greater than 0")


cuadro = clsSquare(10)
cuadro.builSquare()

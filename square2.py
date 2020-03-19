class clsSquare2:
    str1=" "
    str2="*"
    str3 = " *"
    str4 = ""

    def __init__(self,side):    
        self.side = (side)


    def printBase(self):
        print(self.str2 * int(self.side+3))
    def printSide(self):
        for i in range(self.side-1):
           self.str4=(self.str1*(i+1))+self.str2 + (self.str1 * (self.side-(i+1)) + (self.str2))
           print(self.str2+self.str4)


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

cuadro = clsSquare2(10)
cuadro.builSquare()
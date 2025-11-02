 # subtract complex numbers using dunder function

class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img

    def showNum(self):
        print(self.real, 'i + ',self.img,'j')

    # Dunder funciton
    def __sub__(self,num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal,newImg)

# 1st complex number
num1  = Complex(6,7)
num1.showNum()

# 2nd complex number
num2 = Complex(3,4)
num2.showNum()

num3 = num1 - num2 # Now this will work because we have created a dunder function __add__
num3.showNum()
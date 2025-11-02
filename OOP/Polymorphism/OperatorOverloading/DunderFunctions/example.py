# dunder funciton example using complex numbers - adding two complex numbers

class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img

    def showNum(self):
        print(self.real, 'i + ',self.img,'j')

    def add(self,num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal,newImg)

# 1st complex number
num1  = Complex(1,2)
num1.showNum()

# 2nd complex number
num2 = Complex(3,4)
num2.showNum()

num3 = num1.add(num2)
num3.showNum()
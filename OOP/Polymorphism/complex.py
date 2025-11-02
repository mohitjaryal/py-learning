# example

class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img

    def showNum(self):
        print(self.real, 'i + ',self.img,'j')

# 1st complex number
num1  = Complex(1,2)
num1.showNum()

# 2nd complex number
num2 = Complex(3,4)
num2.showNum()
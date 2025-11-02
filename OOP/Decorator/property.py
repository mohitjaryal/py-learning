# @property decorator in py

class Student:
    # Constructor
    def __init__(self,math,phy,chem):
        self.math  = math
        self.phy = phy
        self.chem = chem

    # Average
    @property
    def avg(self):
        return str((self.math + self.phy + self.chem ) / 3 )
    

s1 = Student(100,99,100) # object
print('Old avg :',s1.avg)

# Changing marks
s1.chem = 91
print('New avg :',s1.avg)
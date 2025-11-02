# Define a Circle class to create a circle with radius r using the constructor.
# Define an Area() method of the class which calculates the area of the circle.
# Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle.

class Circle:

    # Constructor
    def __init__(self,r): # r = radius
        self.radius = r

    # Area method 
    def area(self):
        return 3.14 * self.radius ** 2 # formula to calculate area of circle
    
    # Perimeter method
    def perm(self):
        return 2 * 3.14 * self.radius


c1 = Circle(64) # Object of class Circle
print('Area :',c1.area())
print('Perimeter :',c1.perm())
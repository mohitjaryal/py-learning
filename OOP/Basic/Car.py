# Basic dmeonstration of OOP in python

# car class - Mercedes
class Car:
    brand = 'Mercedes'
    model = 'A'
    color = 'Black'
    Year = 2025
    Units = 1000

# car2 class - BMW
class Car2:
    brand = 'BMW'
    model = 'B'
    color = 'White'
    Year = 2025
    Units = 100

# created object - Car class
car1 = Car() 
print('Brand :',car1.brand)
print('Model :',car1.model)
print('Year :',car1.Year)
print('Color :',car1.color)
print('Units :',car1.Units)

car2 = Car2() # created object - Car2 class
print('Brand :',car2.brand)
print('Model :',car2.model)
print('Year :',car2.Year)
print('Color :',car2.color)
print('Units :',car2.Units)
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



car1 = Car() # created object - Car class
print(car1.brand)
print(car1.model)
print(car1.Year)
print(car1.color)
print(car1.Units)

car2 = Car2() # created object - Car2 class
print(car2.brand)
print(car2.model)
print(car2.Year)
print(car2.color)
print(car2.Units)
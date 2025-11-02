# Multi level inheritance

# Parent class
class Car:
    @staticmethod
    def start():
        print('Car started')

    @staticmethod
    def stop():
        print('Car stopped')

# Child class1
class Toyota(Car):  # Inheriting from Car (Parent class)
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

# Child class
class BMW(Car):  # Inheriting from Car (Parent class)
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


t1 = Toyota('Toyota', 'Fortuner')
t1.start()   #  Accessing parent start() method
print(t1.brand)
print(t1.model)
t1.stop()    # Accessing parent stop() method

b1 = BMW('BMW','M5')
t1.start()   #  Accessing parent start() method
print(t1.brand)
print(t1.model)
t1.stop()    # Accessing parent stop() method

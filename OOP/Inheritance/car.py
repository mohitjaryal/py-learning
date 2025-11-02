 # Basic demonstration of inheritance 

class Car:
    @staticmethod
    def start():
        print('Car started ')

    @staticmethod
    def stop():
        print('Car stopped ')

class Toyota:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model


t1 = Toyota('Toyota','Fortuner')
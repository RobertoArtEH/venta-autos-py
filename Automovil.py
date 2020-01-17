class Automovil():
    def __init__(self):
        self.cars = []

    def newCar(self, price):
        self.cars.append(price)

    def getCars(self):
        return self.cars
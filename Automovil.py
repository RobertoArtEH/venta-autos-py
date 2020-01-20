class Automovil():
    def __init__(self):
        self.cars = []

    def newCar(self, brand, model, price):
        self.cars.append({'brand': brand, 'model': model, 'price': price})

    def getCars(self):
        return self.cars
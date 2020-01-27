class Automoviles():
    def __init__(self):
        self.cars = []

    def newCar(self, brand, model, price):
        self.cars.append({'brand': brand, 'model': model, 'price': price})

    def getCars(self):
        return self.cars

    def getCarsComision(self):
        comision = 0

        for car in self.cars:
            comision += car['price']

        comision *= 0.02
        
        return comision
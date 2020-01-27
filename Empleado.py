from Automovil import Automovil

class Empleado():
    def __init__(self, name):
        self.name = name
        self.salary = 2000
        self.bono = 1000
        self.cars = Automovil()

    def getName(self):
        return self.name

    def getSalary(self):
        return self.salary

    def newSale(self, brand, model, price):
        self.salary += self.bono
        self.cars.newCar(brand, model, price)

    def getCars(self):
        return self.cars.getCars()

    def finalSalary(self):
        carsTotal = 0
        cars = self.cars.getCars()

        for car in cars:
            carsTotal += car['price']

        carsTotal = carsTotal * 0.02
        self.salary += carsTotal

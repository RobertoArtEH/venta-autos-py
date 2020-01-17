from Ventas import Ventas
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

    def newSale(self, price):
        self.salary += self.bono
        self.cars.newCar(price)

    def finalSalary(self):
        carsTotal = 0
        car = self.cars.getCars()

        for price in car:
            carsTotal += price

        carsTotal = carsTotal * 0.02
        self.salary += carsTotal

from Empleado import Empleado
from Ventas import Ventas

class Interface():
    def __init__(self):
        self.sales = Ventas()

    def askSale(self):
        return input('¿Agregar un automóvil? (s/n): ')

    def askEmployee(self):
        return input('¿Deseas agregar un nuevo empleado? (s/n): ')

    def employeeSales(self, employee):
        answer = self.askSale()
        while not answer == 'n':
            price = float(input('Ingresa el precio del Automovil: '))
            employee.newSale(price)
            answer = self.askSale()

    def printSalary(self, employee):
        employee.finalSalary()
        salary = employee.getSalary()
        self.sales.newSale(employee)

        print('\x1b[6;30;42m' + '* Salario de {0}: ${1}'.format(employee.getName(), employee.getSalary()) + '\x1b[0m')

    def newEmployee(self):
        name = input('Ingresa nombre de empleado: ')
        employee = Empleado(name)

        self.employeeSales(employee)
        self.printSalary(employee)

    def askNewEmployee(self):
        answer = self.askEmployee()
        while not answer == 'n':
            self.newEmployee()
            answer = self.askEmployee()

    def printEmployees(self):
        print('---------------------')
        print('Lista de empleados:')

        for name in self.sales.getNames():
            print(name)

    def printNomina():
        print('---------------------')
        print('Nomina: ${0}'.format(self.sales.getSales()))

    def run(self):
        self.newEmployee()
        self.askNewEmployee()
        self.printEmployees()
        self.printNomina()
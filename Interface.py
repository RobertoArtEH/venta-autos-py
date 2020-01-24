from Ventas import Ventas
from Empleado import Empleado
from Archivo import Archivo

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
            brand = input('Ingresa la marca del Automovil: ')
            model = input('Ingresa el modelo del Automovil: ')
            price = float(input('Ingresa el precio del Automovil: '))
            employee.newSale(brand, model, price)
            answer = self.askSale()

    def printSalary(self, employee):
        employee.finalSalary()
        salary = employee.getSalary()
        self.sales.newSale(employee)

        print('\x1b[6;30;42m' + '* Salario de {0}: ${1}'.format(employee.getName(), employee.getSalary()) + '\x1b[0m')

    def printCarsSold(self, employee):
        cars = employee.getCars()

        print('\x1b[6;30;42m' + '* Carros vendidos:' + '\x1b[0m')
        for car in cars:
            print('Marca: ' + car['brand'])
            print('Modelo: ' + car['model'])
            print('Precio:', car['price'])
            print('-----------------')

    def newEmployee(self):
        name = input('Ingresa nombre de empleado: ')
        employee = Empleado(name)

        self.employeeSales(employee)
        self.printCarsSold(employee)
        self.printSalary(employee)

    def askNewEmployee(self):
        answer = self.askEmployee()
        print(answer)
        while not answer == 'n':
            self.newEmployee()
            answer = self.askEmployee()

    def printEmployees(self):
        print('---------------------')
        print('Lista de empleados:')

        for name in self.sales.getNames():
            print(name)

    def printNomina(self):
        print('---------------------')
        print('Nomina: ${0}'.format(self.sales.getNomina()))

    def loadFile(self):
        answer = input('¿Deseas cargar el archivo? (s/n): ')
        if(answer == 's'):
            file = Archivo()
            self.sales.setEmployees(file.loadList())
    
    def saveFile(self, employees):
        answer = input('¿Deseas guardar el archivo? (s/n): ')
        if(answer == 's'):
            file = Archivo()
            file.saveList(employees)
            self.printEmployees()

    def run(self):
        self.loadFile()
        self.askNewEmployee()
        self.printEmployees()
        self.printNomina()
        self.saveFile(self.sales.getSales())
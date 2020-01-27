from Ventas import Ventas
from Empleado import Empleado
from Archivo import Archivo

class Interface():
    def __init__(self):
        self.sales = Ventas()

    def employeeSales(self, employee):
        answer = input('¿Agregar un automóvil? (s/n): ')
        while not answer == 'n':
            brand = input('Ingresa la marca del Automovil: ')
            model = input('Ingresa el modelo del Automovil: ')
            price = float(input('Ingresa el precio del Automovil: '))
            employee.newSale(brand, model, price)
            answer = input('¿Agregar un automóvil? (s/n): ')

    def printSalary(self, employee):
        employee.finalSalary()
        salary = employee.getSalary()
        self.sales.newEmployee(employee)

        print('\x1b[6;30;42m' + '* Salario de {0}: ${1}'.format(employee.getName(), employee.getSalary()) + '\x1b[0m')

    def printCarsSold(self, employee):
        cars = employee.getCars()

        print('\x1b[6;30;42m' + '* Carros vendidos:' + '\x1b[0m')
        for car in cars:
            print('Marca: ' + car['brand'])
            print('Modelo: ' + car['model'])
            print('Precio:', car['price'])
            print('****')

    def addNewEmployee(self):
        name = input('Ingresa nombre de empleado: ')
        employee = Empleado(name)

        self.employeeSales(employee)
        self.printCarsSold(employee)
        self.printSalary(employee)

    def askNewEmployee(self):
        answer = input('¿Deseas agregar un nuevo empleado? (s/n): ')
        while not answer == 'n':
            self.addNewEmployee()
            answer = input('¿Deseas agregar un nuevo empleado? (s/n): ')

    def printEmployees(self):
        print('****')
        print('Lista de empleados:')

        for name in self.sales.getNames():
            print(name)

    def printNomina(self):
        print('****')
        print('\x1b[6;30;42m' + '* Nomina: ${0}'.format(self.sales.getNomina()) + '\x1b[0m')

    def loadFile(self):
        try:
            with open('sales_list') as f:
                file = Archivo()
                self.sales.setEmployees(file.loadList())
        except IOError:
            print('No se encontró ningun reporte...')
    
    def saveFile(self, employees):
        answer = input('¿Deseas guardar el archivo? (s/n): ')
        if(answer == 's'):
            file = Archivo()
            file.saveList(employees)
            self.printEmployees()

    def run(self):
        self.loadFile()
        self.addNewEmployee()
        self.askNewEmployee()
        self.printEmployees()
        self.printNomina()
        self.saveFile(self.sales.getEmployees())
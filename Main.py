from Empleado import Empleado
from Ventas import Ventas

sales = Ventas()

def askSale():
    return input('¿Vendio un automóvil? (s/n): ')

def askNewEmployee():
    return input('¿Deseas agregar un nuevo empleado? (s/n): ')

# Proceso de nuevo empleado
def newEmployee():
    name = input('Ingresa nombre de empleado: ')
    employee = Empleado(name)

    answer = askSale()
    while not answer == 'n':
        price = float(input('Ingresa el precio del Automovil: '))
        employee.newSale(price)
        answer = askSale()

    employee.finalSalary()
    salary = employee.getSalary()
    sales.newSale(employee)
    print('\x1b[6;30;42m' + '* Salario de {0}: ${1}'.format(employee.getName(), employee.getSalary()) + '\x1b[0m')

def run():
    newEmployee()
    answer = askNewEmployee()
    while not answer == 'n':
        newEmployee()
        answer = askNewEmployee()
    
    print('---------------------')
    print('Lista de empleados:')

    for name in sales.getNames():
        print(name)
    
    print('---------------------')
    print('Nomina: ${0}'.format(sales.getSales()))

run()
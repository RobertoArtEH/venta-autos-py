class Ventas():
    def __init__(self):
        self.sales = []

    def newSale(self, empleado):
        self.sales.append(empleado)

    def getSales(self):
        return self.sales

    def getNames(self):
        names = []

        for employee in self.sales:
            names.append(employee.name)

        return names

    def getNomina(self):
        nomina = 0

        for employee in self.sales:
            nomina += employee.salary

        return nomina

    def setEmployees(self, employees):
        self.sales = employees
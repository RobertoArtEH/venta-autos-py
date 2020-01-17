class Ventas():
    def __init__(self):
        self.sales = []

    def newSale(self, empleado):
        self.sales.append(empleado)

    def getNames(self):
        names = []

        for employee in self.sales:
            names.append(employee.name)

        return names

    def getSales(self):
        nomina = 0

        for employee in self.sales:
            nomina += employee.salary

        return nomina
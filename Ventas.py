class Ventas():
    def __init__(self):
        self.employees = []

    def newEmployee(self, employee):
        self.employees.append(employee)

    def getEmployees(self):
        return self.employees

    def setEmployees(self, employees):
        self.employees = employees

    def getNames(self):
        names = []

        for employee in self.employees:
            names.append(employee.name)

        return names

    def getNomina(self):
        nomina = 0

        for employee in self.employees:
            nomina += employee.salary

        return nomina
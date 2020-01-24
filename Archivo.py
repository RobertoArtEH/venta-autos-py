import pickle

class Archivo():
    def __init__(self):
        self.employees = []

    def saveList(self, employees):
        print('\x1b[6;30;42m' + 'Menú de Reportes' + '\x1b[0m')
        print('1) Guardar reporte')
        print('2) Salir')
        option = input('Selecciona la opción que desees: ')

        if(option == '1'):
            fichero_binario = open("sales_list","wb")
            pickle.dump(employees, fichero_binario)
            fichero_binario.close()
            del(fichero_binario)

    def loadList(self):
        fichero = open("sales_list", "rb")
        self.employees = pickle.load(fichero)
        
        return self.employees
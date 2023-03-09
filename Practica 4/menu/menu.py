import os
from planificadores.planificadores import Planificadores

class Menu:

    def __init__(self, file_path) -> None:
        
        self.planificador = Planificadores(file_path)
        self.planificador.load_processes()

    def menu_principal(self):
        continuar = True
        while continuar:
            print("\n\n\nSeleccione un algoritmo de planificación:")
            print("1. Round Robin")
            print("2. SJF")
            print("3. FIFO")
            print("4. Prioridades")
            opcion = int(input("Ingrese la opción deseada: "))
            if opcion == 1:
                quantum = int(input("Ingrese el valor del quantum: "))
                if(self.menu_insertar_procesos()):
                    self.planificador.add_process()
                self.planificador.round_robin(quantum)
            elif opcion == 2:
                if(self.menu_insertar_procesos()):
                    self.planificador.add_process()
                self.planificador.sjf()
            elif opcion == 3:
                if(self.menu_insertar_procesos()):
                    self.planificador.add_process()
                self.planificador.fifo()
            elif opcion == 4:
                if(self.menu_insertar_procesos()):
                    self.planificador.add_process()
                self.planificador.prioridades()
            else:
                print("Opción inválida.")
            
            continuar_opcion = input("¿Desea continuar? (S/N)").lower()
            if continuar_opcion == 'n':
                continuar = False
            os.system("CLS")

    def menu_insertar_procesos(self):
        opc = input("¿Desea agregar procesos? (S/N)").lower()
        agregar = True
        if opc == 'n':
            agregar = False
        return agregar


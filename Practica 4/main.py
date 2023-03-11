# -*- coding: utf-8 -*-
"""
Created on Sat Mar  8 23:54:21 2023

@author: Manuel

Algoritmos de planificacion
"""

from planificadores.planificadores import Planificadores 


if __name__ == "__main__":
     planificador = Planificadores("./procesos.txt")
     planificador.load_processes()
     while True:
        print("\n\n\nSeleccione un algoritmo de planificación:")
        print("1. Round Robin")
        print("2. SJF")
        print("3. FIFO")
        print("4. Prioridades")
        print("5. Ingresar nuevos procesos")
        print("0. Salir")
        opcion = int(input("Ingrese la opción deseada: "))
        if opcion == 1:
            quantum = int(input("Ingrese el valor del quantum: "))
            planificador.round_robin(quantum)
        elif opcion == 2:
            planificador.sjf()
        elif opcion == 3:
            planificador.fifo()
        elif opcion == 4:
            planificador.prioridades()
        elif opcion == 5:
            planificador.add_process()
        elif opcion == 0:
            break
        else:
            print("Opción inválida.")





# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 23:54:21 2023

@author: Manuel

Algoritmos de planificacion
"""

import heapq
from collections import deque

class Planificadores:

    def __init__(self, file_path):
        self.file_path = file_path

    def open_file(self):
        # Abre el archivo de procesos y devuelve una lista con los procesos
        with open(self.file_path, 'r') as file:
            lst = []
            for element in file.readlines():
                lst.append(element.split("\n")[0])
            return lst

    def round_robin(self, quantum):
        lst = [element.split(",")[:2] for element in self.open_file()]
        processes = [(pid, int(pt)) for pid, pt in lst]
        queue = deque(processes)
        while queue:
            current_process = queue.popleft()
            process_id, process_time = current_process
            print(f"Ejecutando proceso {process_id}")
            process_time -= quantum
            if process_time > 0:
                queue.append((process_id, process_time))
                print(f"Proceso {process_id} regresado a la cola con {process_time} unidades de tiempo restantes")
            else:
                print(f"Proceso {process_id} terminado")

    def sjf(self):
        lst = [element.split(",")[:2] for element in self.open_file()]
        processes = [(pid, int(pt)) for pid, pt in lst]
        queue = []
        for process in processes:
            heapq.heappush(queue, (process[1], process))

        while queue:
            # Obtener el proceso con menor tiempo restante
            _, current_process = heapq.heappop(queue)
            process_id, process_time = current_process
            print(f"Ejecutando proceso {process_id} durante {process_time} unidades de tiempo")
            print(f"Proceso {process_id} terminado")

    def fifo(self):
        lst = [element.split(",")[:1] for element in self.open_file()]
        lst = [process[0] for process in lst]
        for i in range(len(lst)):
            terminado = lst.pop(0)
            print(f"Ejecutando proceso {terminado}")
            print(f"Proceso {terminado} terminado.\n")

    def prioridades(self):
        lst = [element.split(",")[::2] for element in self.open_file()]
        processes = [(pid, int(pt)) for pid, pt in lst]
        queue = []
        for process in processes:
            heapq.heappush(queue, (process[1], process))

        while queue:
            # Obtener el proceso con mas prioridad
            _, current_process = heapq.heappop(queue)
            process_id, process_priority = current_process
            print(f"Ejecutando proceso {process_id} con prioridad {process_priority}")
            print(f"Proceso {process_id} terminado\n")



if __name__ == "__main__":
    plan = Planificadores("./procesos.txt")
    plan.fifo()


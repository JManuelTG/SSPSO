import heapq
from collections import deque
import os

class Planificadores:
    def __init__(self, file_path):
        self.file_path = file_path
        self.processes = []

    def load_processes(self):
        # Lee los procesos del archivo y los agrega a la lista de procesos
        with open(self.file_path, 'r') as file:
            for element in file.readlines():
                pid, pt, priority = element.split(",")
                self.processes.append((pid, int(pt), int(priority)))


    def add_process(self):
        # Agrega un nuevo proceso a la lista de procesos
        while True:
            try:
                pid = input("Ingrese el nombre del proceso: ")
                pt = int(input("Ingrese el tiempo de duración del proceso: "))
                priority = int(input("Ingrese la prioridad del proceso: "))
                position = int(input("Ingrese la posición donde desea agregar el proceso: 0 == Inicio, 1 == Final "))
                if position  == 0:
                    self.processes.insert(0, (pid, pt, priority))
                else:
                    self.processes.append((pid, pt, priority))
                break
            except ValueError:
                print("Debe ingresar un número entero.")



    def round_robin(self):
        quantum = 3
        os.system("CLS")
        queue = deque(self.processes)
        while queue:
            current_process = queue.popleft()
            process_id, process_time, process_priority = current_process
            print(f"Ejecutando proceso '{process_id}' ")
            process_time -= quantum
            if process_time > 0:
                queue.append((process_id, process_time, process_priority))
                print(f"Proceso {process_id} regresado a la cola con {process_time} unidades de tiempo restantes\n")
            else:
                print(f"Proceso {process_id} terminado\n")


    def sjf(self):
        os.system("CLS")
        queue = []
        for process in self.processes:
            heapq.heappush(queue, (process[1], process))

        while queue:
            # Obtener el proceso con menor tiempo restante
            _, current_process = heapq.heappop(queue)
            process_id, process_time, process_priority = current_process
            print(f"Ejecutando proceso {process_id} durante {process_time} unidades de tiempo")
            print(f"Proceso {process_id} terminado\n")


    def fifo(self):
        os.system("CLS")
        for process in self.processes:
            process_id, process_time, process_priority = process
            print(f"Ejecutando proceso {process_id}")
            print(f"Proceso {process_id} terminado\n")


    def prioridades(self):
        os.system("CLS")
        queue = []
        for process in self.processes:
            heapq.heappush(queue, (process[2], process))

        while queue:
            # Obtener el proceso con más prioridad
            _, current_process = heapq.heappop(queue)
            process_id, process_time, process_priority = current_process
            print(f"Ejecutando proceso {process_id} con prioridad {process_priority}")
            print(f"Proceso {process_id} terminado\n")
    
    def get_procesos(self):
        return self.processes
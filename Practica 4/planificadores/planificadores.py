import heapq
from collections import deque

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
        pid = input("Ingrese el nombre del proceso: ")
        pt = int(input("Ingrese el tiempo de duración del proceso: "))
        priority = int(input("Ingrese la prioridad del proceso: "))
        position = int(input("Ingrese la posición donde desea agregar el proceso (al principio o al final): "))
        print("\n\n")
        if position >= 0 and position < len(self.processes):
            self.processes.insert(position, (pid, pt, priority))
        else:
            self.processes.append((pid, pt, priority))


    def round_robin(self, quantum):
        queue = deque(self.processes)
        while queue:
            current_process = queue.popleft()
            process_id, process_time, process_priority = current_process
            print(f"Ejecutando proceso {process_id}")
            process_time -= quantum
            if process_time > 0:
                queue.append((process_id, process_time, process_priority))
                print(f"Proceso {process_id} regresado a la cola con {process_time} unidades de tiempo restantes")
            else:
                print(f"Proceso {process_id} terminado")


    def sjf(self):
        queue = []
        for process in self.processes:
            heapq.heappush(queue, (process[1], process))

        while queue:
            # Obtener el proceso con menor tiempo restante
            _, current_process = heapq.heappop(queue)
            process_id, process_time, process_priority = current_process
            print(f"Ejecutando proceso {process_id} durante {process_time} unidades de tiempo")
            print(f"Proceso {process_id} terminado")


    def fifo(self):
        for process in self.processes:
            process_id, process_time, process_priority = process
            print(f"Ejecutando proceso {process_id}")
            print(f"Proceso {process_id} terminado\n")


    def prioridades(self):
        queue = []
        for process in self.processes:
            heapq.heappush(queue, (process[2], process))

        while queue:
            # Obtener el proceso con más prioridad
            _, current_process = heapq.heappop(queue)
            process_id, process_time, process_priority = current_process
            print(f"Ejecutando proceso {process_id} con prioridad {process_priority}")
            print(f"Proceso {process_id} terminado")
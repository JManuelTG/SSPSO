"""Algoritmos de planificacion"""\

import heapq
from collections import deque


def open_file(file_path):
    #Abre el archivo de procesos y devuelve una lista con los procesos
    with open(file_path, 'r') as file:
        lst = []
        for element in file.readlines():
            lst.append(element.split("\n")[0])
        return lst


def round_robin(quantum):

    lst = [element.split(",")[:2] for element in open_file("./procesos.txt")]
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


def sjf():

    lst = [element.split(",")[:2] for element in open_file("./procesos.txt")]
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


def fifo():
    lst = [element.split(",")[:1] for element in open_file("./procesos.txt")]
    lst = [process[0] for process in lst]
    for i in range(len(lst)-1,-1,-1):
        terminado = lst.pop(0)
        print(f"Ejecutando proceso {terminado}")
        print(f"Proceso {terminado} terminado.\n")


def prioridades():
    
    lst = [element.split(",")[::2] for element in open_file("./procesos.txt")]
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
    #round_robin(3)
    #sjf()
    fifo()
    #prioridades()

from tkinter import *
from tkinter import ttk
from planificadores.planificadores import Planificadores

class App():

    def __init__(self,master) -> None:
        self.frame = ttk.Frame(master)
        self.frame.pack(fill=BOTH, expand=True)
       
        self.planificadores = Planificadores('procesos.txt')
        self.planificadores.load_processes()

        master.title("Planificadores")
        master.geometry("1290x720")
        master.iconbitmap("planificador.ico")
        
        self.create_sidebar()


    def create_sidebar(self):
        sidebar = Frame(self.frame, width=200, bg='gray')
        sidebar.pack(side=LEFT, fill=Y)

        ttk.Style().configure('TButton', padding=10, relief="flat", background="#ccc", foreground="black")
        ttk.Button(sidebar, text="Round Robin", command=self.round_robin_handler).pack(pady=10)
        ttk.Button(sidebar, text="SJF", command=self.sjf_handler).pack(pady=10)
        ttk.Button(sidebar, text="FIFO", command=self.fifo_handler).pack(pady=10)
        ttk.Button(sidebar, text="Prioridades", command=self.prioridades_handler).pack(pady=10)
        ttk.Button(sidebar, text="Salir", command=self.frame.quit).pack(side=BOTTOM, pady=10)


    def round_robin_handler(self):
        quantum = 2
        self.planificadores.round_robin(quantum)

    def sjf_handler(self):
        self.planificadores.sjf()

    def fifo_handler(self):
        self.planificadores.fifo()

    def prioridades_handler(self):
        self.planificadores.prioridades()


        
from tkinter import *
from tkinter import ttk
from planificadores.planificadores import Planificadores
import random 

class App():

    def __init__(self,master) -> None:
        super().__init__()
        self.frame = ttk.Frame(master)
        self.frame.pack(fill=BOTH, expand=True)

        master.title("Planificadores")
        master.geometry("1000x600")
        master.iconbitmap("planificador.ico")  
       
        self.planificadores = Planificadores('procesos.txt')
        self.planificadores.load_processes()


    
        #Panel iziquierdo
        sidebar = Frame(self.frame, bd=1, width=400, bg="#2F2F2F",borderwidth=2)
        sidebar.pack(side=LEFT, fill=Y)


        ttk.Style().configure('TButton', padding=10, relief="flat", background="#ccc", foreground="black")
        ttk.Button(sidebar, text="Round Robin", command=self.round_robin_handler).pack(pady=10)
        ttk.Button(sidebar, text="SJF", command=self.sjf_handler).pack(pady=10)
        ttk.Button(sidebar, text="FIFO", command=self.fifo_handler).pack(pady=10)
        ttk.Button(sidebar, text="Prioridades", command=self.prioridades_handler).pack(pady=10)
        ttk.Button(sidebar, text="Agregar", command="").pack(pady=10)
        ttk.Button(sidebar, text="Salir", command=self.frame.quit).pack(side=BOTTOM, pady=10)

        #Panel derecho
        content = Frame(self.frame, bd=1, bg="#D3D0CB", borderwidth=2)
        content.pack(side=LEFT, fill=BOTH, expand=True)

        # Separador
        canvas = Canvas(content, height=2, highlightthickness=0)
        canvas.create_line(0, 0, 1000, 0, fill="#2F2F2F")
        canvas.pack(fill=X)

        #Panel derecho inferior
        abajo = Frame(content,bd=1,bg="#D3D0CB",borderwidth=2)
        abajo.pack(side=BOTTOM,fill=BOTH,expand=True)


    def round_robin_handler(self):
        self.planificadores.round_robin(3)


    def sjf_handler(self):
        self.planificadores.sjf()


    def fifo_handler(self):
        self.planificadores.fifo()


    def prioridades_handler(self):
        self.planificadores.prioridades()
       


        
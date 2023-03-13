from tkinter import *
from tkinter import ttk
from planificadores.planificadores import Planificadores

class App():

    def __init__(self,master) -> None:
        super().__init__()
        self.frame = ttk.Frame(master)
        self.frame.pack(fill=BOTH, expand=True)

        master.title("Planificadores")
        master.geometry("1280x720")
        master.iconbitmap("planificador.ico")  
       
        self.planificadores = Planificadores('procesos.txt')
        self.planificadores.load_processes()
    
        #Panel iziquierdo
        sidebar = Frame(self.frame, bd=1, padx=40, bg="#2F2F2F",borderwidth=2)
        sidebar.pack(side=LEFT, fill=Y)
        #Etiqueta Opciones
        sidebar_label = Label(sidebar,text="Opciones", bg="#2F2F2F", foreground="#FFFFFF")
        sidebar_label.pack()

        ttk.Style().configure('TButton', padding=10, relief="flat", background="#ccc", foreground="black")
        ttk.Button(sidebar, text="Round Robin", command=self.planificadores.round_robin).pack(pady=10)
        ttk.Button(sidebar, text="SJF", command=self.planificadores.sjf).pack(pady=10)
        ttk.Button(sidebar, text="FIFO", command=self.planificadores.fifo).pack(pady=10)
        ttk.Button(sidebar, text="Prioridades", command=self.planificadores.prioridades).pack(pady=10)
        ttk.Button(sidebar, text="Agregar", command="").pack(pady=10)
        ttk.Button(sidebar, text="Salir", command=self.frame.quit).pack(side=BOTTOM, pady=10)

        #Panel derecho
        content = Frame(self.frame, bd=1, bg="#D3D0CB", borderwidth=2)
        content.pack(side=LEFT, fill=BOTH, expand=True)

        #Etiqueta Contenido
        content_label = Label(content,text="Procesos", bg="#D3D0CB",font=15)
        content_label.pack()

        # Crear objeto Treeview
        table = ttk.Treeview(content,yscrollcommand="none",show='headings')

        # Agregar columnas
        table['columns'] = ('ID', 'Tiempo', 'Prioridad')
        table.column('ID', anchor='center', width=100)
        table.column('Tiempo', anchor='center', width=100)
        table.column('Prioridad', anchor='center', width=100)

        # Agregar encabezados
        table.heading('ID', text='ID', anchor='center')
        table.heading('Tiempo', text='Tiempo', anchor='center')
        table.heading('Prioridad', text='Prioridad', anchor='center')

        for item in self.planificadores.get_procesos():
            table.insert('','end', values=item)
        table.pack(fill=X,padx=10,pady=5)


        # Separador
        canvas = Canvas(content, height=4, highlightthickness=0)
        canvas.create_line(0, 0, 1000, 0, fill="#2F2F2F")
        canvas.pack(fill=X)


        #Panel derecho inferior
        abajo = Frame(content,bd=1,bg="#D3D0CB",borderwidth=2)
        abajo.pack(side=BOTTOM,fill=BOTH,expand=True)

       


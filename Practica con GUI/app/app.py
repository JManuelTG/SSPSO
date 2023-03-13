from tkinter import *
from tkinter import ttk, messagebox
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
        ttk.Button(sidebar, text="Agregar", command=self.add_process).pack(pady=10)
        ttk.Button(sidebar, text="Actualiza", command=self.actualizar_tabla).pack(pady=10)
        ttk.Button(sidebar, text="Salir", command=self.frame.quit).pack(side=BOTTOM, pady=10)

        #Panel derecho
        content = Frame(self.frame, bd=1, bg="#D3D0CB", borderwidth=2)
        content.pack(side=LEFT, fill=BOTH, expand=True)

        #Panel para tabla
        frame_table = LabelFrame(content,text="Procesos",font=10,padx=10,pady=10,height=100,bg="#D3D0CB")
        frame_table.pack(padx=10,pady=10, fill=X)

        # Crear objeto Treeview
        self.table = ttk.Treeview(frame_table,yscrollcommand="none",show='headings')

        # Agregar columnas
        self.table['columns'] = ('ID', 'Tiempo', 'Prioridad')
        self.table.column('ID', anchor='center', width=100)
        self.table.column('Tiempo', anchor='center', width=100)
        self.table.column('Prioridad', anchor='center', width=100)

        # Agregar encabezados
        self.table.heading('ID', text='ID', anchor='center')
        self.table.heading('Tiempo', text='Tiempo', anchor='center')
        self.table.heading('Prioridad', text='Prioridad', anchor='center')

        self.actualizar_tabla()

        # Separador
        canvas = Canvas(content, height=4, highlightthickness=0)
        canvas.create_line(0, 0, 1280, 0, fill="#2F2F2F")
        canvas.pack(fill=X)

        #Panel derecho inferior
        abajo = Frame(content,bd=1,bg="#D3D0CB",borderwidth=2)
        abajo.pack(side=BOTTOM,fill=BOTH,expand=True)

    def actualizar_tabla(self):
        for row in self.table.get_children():
            self.table.delete(row)
        for item in self.planificadores.get_procesos():
            self.table.insert('','end', values=item)
        self.table.pack(fill=X,padx=10,pady=5)

    def add_process(self):
        ventana = Toplevel()
        ventana.title("Agregar procesos")
        ventana.geometry("500x205")
        ventana.iconbitmap("planificador.ico")

        top = Frame(ventana,bd=1, padx=40, bg="#2F2F2F",borderwidth=2, height=20)
        top.pack(side=TOP, fill=X, expand=False)
        frame = Frame(ventana,padx=40,bg="#D3D0CB")
        frame.pack(expand=False, fill=BOTH)

        id_proceso = Entry(frame, width=40)
        id_proceso.grid(row=0,column=1,pady=10)
        id_label = Label(frame, text="ID Proceso:", bg="#D3D0CB")
        id_label.grid(row=0,column=0,padx=20,pady=10)

        tiempo = Entry(frame, width=40)
        tiempo.grid(row=1,column=1,pady=10)
        tiempo_label = Label(frame, text="Tiempo:", bg="#D3D0CB")
        tiempo_label.grid(row=1,column=0,padx=20,pady=10)

        prioridad = Entry(frame, width=40)
        prioridad.grid(row=2,column=1,pady=10)
        prioridad_label = Label(frame, text="Prioridad:", bg="#D3D0CB")
        prioridad_label.grid(row=2,column=0,padx=20,pady=10)

        ttk.Button(frame, text="Agregar", command=lambda: (self.planificadores.add_process(id_proceso.get(),int(tiempo.get()),int(prioridad.get())),
                                                           messagebox.showinfo("Aviso","Proceso agregado con exito"))).grid(row=4,column=0,pady=10)
        ttk.Button(frame, text="Salir", command=ventana.destroy).grid(row=4,column=2,pady=10)

 


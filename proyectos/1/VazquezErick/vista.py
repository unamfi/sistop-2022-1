import tkinter
import threading

WIDTH = 800
HEIGHT = 640

class Vista(threading.Thread):

    def __init__(self, controlador):
        
        self.controlador = controlador
        self.ventana = tkinter.Tk()
        self.ventana.title("Puesto de tacos")

        # se bloquea el redimensionado de la ventana
        self.ventana.resizable(0, 0)

        # frame de inicio del programa
        self.inicio = tkinter.Frame()
        # se define el tamanio de la ventana
        self.inicio.config(width=WIDTH, height=HEIGHT)
        self.inicio.pack()

        title = tkinter.Label(self.inicio, text="Puesto de tacos", font=(None, 30))
        title.grid(row=0, column=1)

        mensaje = tkinter.Label(self.inicio, text="Ingrese el # de clientes que quiere generar: ")
        mensaje.grid(row=1, column=0, pady=20)

        self.caja_num_clientes = tkinter.Entry(self.inicio)
        self.caja_num_clientes.config()
        self.caja_num_clientes.grid(row=1, column=2)

        boton_inicio = tkinter.Button(self.inicio, text="Iniciar", command=self.empezar)
        boton_inicio.grid(row=2, column=1)

        self.texto_error = tkinter.StringVar()
        mensaje_error = tkinter.Label(self.inicio, textvariable=self.texto_error)
        mensaje_error.grid(row=3, column=1, pady=20)

    def inicia_interfaz(self):
        # loop principal de la app
        self.ventana.mainloop()
    
    def empezar(self):
        num_clientes = self.caja_num_clientes.get()
        if not num_clientes.isdigit():
            self.texto_error.set("Ingresa un numero, por favor")
        else:
            num_clientes = int(num_clientes)
            self.controlador.inicia_programa(num_clientes)
            self.ventana.destroy()
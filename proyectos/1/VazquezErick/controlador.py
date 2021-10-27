import threading


class Controlador:

    def __init__(self):
        self.esperando_inicio = threading.Semaphore(0)
        self.num_clientes = 0

    def inicia_programa(self, num_clientes):
        self.num_clientes = num_clientes
        self.esperando_inicio.release()


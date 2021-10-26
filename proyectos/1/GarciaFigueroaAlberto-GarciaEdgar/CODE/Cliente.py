#from CODE.Empleado import Empleado
import threading
class Cliente(object):

    def __init__(self,id,tienda):
        self.numero = id 
        self.tienda = tienda
        global CajaCliente
        CajaCliente=threading.Semaphore(0)

    def entrar(self):
        print("Cliente "+str(self.numero)+" quiere entrar a la tienda")
        self.tienda.pass_client(self)

    def agarra(self):
        if self.tienda.estante <15:
            print("El cliente"+str(self.numero)+"notifica que se acaban los productos...")
            self.tienda.checarEstante()
        print("El cliente"+str(self.numero)+" agarra los productos")
        self.pagar()
    
    def pagar(self):
        self.tienda.CajaCliente.release()
        self.tienda.CajaEmpleado.acquire()
        print("El cliente "+str(self.numero)+" ha pagado sus productos")
        self.salir()
    
    def salir(self):
        print("El cliente"+str(self.numero)+" abandona la tienda")
        self.tienda.leave_client(self)